const { dyeBucket, loadItems, dyePixel, getMapState, getCurrentPacket, getMostUsed, getNeededDyes, saveImage } = require('Art-functions.ts');

const name = "Junji";

const status = FS.open('Jsons/status.json');
let {processing, toBeProcessed, alreadyProcessed} = JSON.parse(status.read());

if(toBeProcessed.length == 0) {
  Chat.log("No images to be done"); 
}

if(!processing || processing == "") {
  processing = toBeProcessed.shift();
  status.write(JSON.stringify({processing, toBeProcessed, alreadyProcessed}));
}



const positions = JSON.parse(FS.open("Positions.json").read());
const AntiAfk = JsMacros.runScript("scripts/Project-art/scripts/Anti-afk.ts");
const dyesJson = JSON.parse(FS.open(`Jsons/${processing}`).read());

////////////////Start
const startingTime = Time.time();

//Get the client instance:
let clientInstance = Client.getMinecraft();
//Use reflection to get the Minecraft class
let MapUpdateS2CPacket = Reflection.getClass("net.minecraft.class_2683");
//Use reflection to get the field that holds the update data
let updateData = Reflection.getDeclaredField(MapUpdateS2CPacket, "comp_2274"); //1.19.2 field_28016
//let id = Reflection.getDeclaredMethod(MapUpdateS2CPacket, "method_11644");

let MapState = Reflection.getClass("net.minecraft.class_22$class_5637");
let width = Reflection.getDeclaredField(MapState, "comp_2318"); // 1.19.2 field_27894
let height = Reflection.getDeclaredField(MapState, "comp_2319"); // 1.19.2 field_27895
let colors = Reflection.getDeclaredField(MapState, "comp_2320"); // 1.19.2 field_27896


updateData.setAccessible(true);
width.setAccessible(true);
height.setAccessible(true);
colors.setAccessible(true);

//id.setAccessible(true);



let packet;

const listenerPacket = JsMacros.on("RecvPacket", JavaWrapper.methodToJava(event => {
  if (event.type !== "MapUpdateS2CPacket") return;

  let updateDataObj = updateData.get(event.packet);
  if (updateDataObj == null) return;

  // Check if updateDataObj is an Optional and retrieve the actual value
  if (updateDataObj instanceof java.util.Optional) {
      // Get the actual value contained in the Optional
      let actualUpdateDataObj = updateDataObj.isPresent() ? updateDataObj.get() : null;
      
      if (actualUpdateDataObj == null) {
          //Chat.log("No value present in Optional.");
          return;
      }

      // Try to get the width and height
      try {
          const widthObj = width.get(actualUpdateDataObj);
          const heightObj = height.get(actualUpdateDataObj);

          if (widthObj != 128 || heightObj != 128) return;

          let colorsObj = colors.get(actualUpdateDataObj);
          if (colorsObj == null) return;
          packet = colorsObj;
      } catch (error) {
          Chat.log("Error accessing fields: " + error);
      }
  } else {
      Chat.log("UpdateData Object is not an Optional.");
  }
}));

let inv = Player.openInventory()
const mapSlot = inv.findItem("minecraft:filled_map")[0];
const mapSlotName = inv.getSlot(mapSlot).getName().getString();

if(mapSlot && mapSlotName != "template") inv.dropSlot(mapSlot); //template name is for canvas maps used for starting the art



getCurrentPacket();
Client.waitTick(5);
if(!packet) {
  getCurrentPacket();
  Client.waitTick(5);
}
let dyes = getMapState(packet, dyesJson, true);

if(!dyes) {
  const mostUsed = getMostUsed(dyesJson);
  const feather = "minecraft:feather"
  const coal = "minecraft:coal"
  const bucket = "minecraft:bucket"
  const items = [bucket, coal, feather, mostUsed.slice(0, -1)];
  loadItems(items);
  dyeBucket(Player.openInventory(), mostUsed);
  Client.waitTick(10);
  getCurrentPacket(); 
  Client.waitTick(5);
  dyes = getMapState(packet, dyesJson, false);
}
Client.waitTick(5);


let neededDyes = getNeededDyes(dyes);

loadItems(neededDyes)
let interations = 0;
let end = false;
while(!end) {
  end = true;
  for (let dye in neededDyes) {
    for (const info in dyes) {
      if(neededDyes[dye].replace("minecraft:", "") != dyes[info][1][0]) { continue }
      if(dyes[info][1][0] == "done") { continue };

      let success = dyePixel(inv, positions[dyes[info][0]], neededDyes[dye])
      if(success == -1) {
        //Chat.log("Failed to dye " + neededDyes[dye])
        loadItems([neededDyes[dye]])
        Client.waitTick()
        dyePixel(inv, positions[dyes[info][0]], neededDyes[dye])
      }
      end = false;
      interations++;
    }
  }
  dyes = getMapState(packet, dyesJson, false);
  neededDyes = getNeededDyes(dyes);
}


//Finishing
saveImage(name + "_" + processing.match(/\d+/));
alreadyProcessed.push(processing);
processing = "";
status.write(JSON.stringify({processing, toBeProcessed, alreadyProcessed}));
AntiAfk.getCtx().closeContext();
listenerPacket.off();
const endingTime = Time.time();
Chat.log("Art done in: " + ((endingTime - startingTime)/1000) + "s");
Chat.log("Iterations: " + interations);

if(toBeProcessed.length != 0) {
  JsMacros.runScript("scripts/Project-art/scripts/Project-Art.ts");
}

/*
// Iterate over original array and assign elements to 2D array
for (let i = 0; i < values.length; i++) {
  const row = Math.floor(i / 32);
  const col = i % 32;
  matrix[row][col] = values[i];
}


FS.open("neededDyes.json").write(JSON.stringify(matrix));
FS.open("dye.json").write(JSON.stringify(dyesJson));
*/