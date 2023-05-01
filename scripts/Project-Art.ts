const { dyeBucket, loadItems, dyePixel, getMapState, getCurrentPacket, getMostUsed, getNeededDyes } = require('Art-functions.ts');

const startingTime = Time.time();

////////////////Start

//Get the client instance:
let clientInstance = Client.getMinecraft();
//Use reflection to get the Minecraft class
let MapUpdateS2CPacket = Reflection.getClass("net.minecraft.class_2683");
//Use reflection to get the field that holds the update data
let updateData = Reflection.getDeclaredField(MapUpdateS2CPacket, "field_28016");
//let id = Reflection.getDeclaredMethod(MapUpdateS2CPacket, "method_11644");

let MapState = Reflection.getClass("net.minecraft.class_22$class_5637");
let width = Reflection.getDeclaredField(MapState, "field_27894");
let height = Reflection.getDeclaredField(MapState, "field_27895");
let colors = Reflection.getDeclaredField(MapState, "field_27896");


updateData.setAccessible(true);
width.setAccessible(true);
height.setAccessible(true);
colors.setAccessible(true);
//id.setAccessible(true);

let packet;

const listener = JsMacros.on("RecvPacket", JavaWrapper.methodToJava(event => {
    if (event.type !== "MapUpdateS2CPacket") return;

    let updateDataObj = updateData.get(event.packet);
    if (updateDataObj == null) return;
    
    //const idObj = id.invoke(event.packet);
    const widthObj = width.getInt(updateDataObj);
    const heightObj = height.getInt(updateDataObj);
    
    if(widthObj != 128 || heightObj != 128) return;
    let colorsObj = colors.get(updateDataObj);
    if (colorsObj == null) return;
    packet = colorsObj;
}));


const positions = JSON.parse(FS.open("Positions.json").read());
const AntiAfk = JsMacros.runScript("scripts/Project-art/scripts/Anti-afk.ts");
const dyesJson = JSON.parse(FS.open("similar_colors.json").read());


getCurrentPacket();
Client.waitTick(5);
let dyes = getMapState(packet, dyesJson, true);

if(!dyes) {
  const mostUsed = getMostUsed(dyesJson);
  const feather = "minecraft:feather"
  const coal = "minecraft:coal"
  const bucket = "minecraft:bucket"
  const items = [bucket, coal, feather, mostUsed.slice(0, -1)];
  loadItems(items);
  dyeBucket(Player.openInventory(), mostUsed);
  Client.waitTick(5);
  getCurrentPacket(); 
  Client.waitTick(5);
  dyes = getMapState(packet, dyesJson, false);
}
Client.waitTick(5);


let neededDyes = getNeededDyes(dyes);

loadItems(neededDyes)
let inv = Player.openInventory()
let end = false;
while(!end) {
  end = true;
  for (let dye in neededDyes) {
    for (const info in dyes) {
      if(neededDyes[dye].replace("minecraft:", "") != dyes[info][1][0]) { continue }
      if(dyes[info][1][0] == "done") { continue };
      let success = dyePixel(inv, positions[dyes[info][0]], neededDyes[dye])
      if(success == -1) {
        Chat.log("Failed to dye " + neededDyes[dye])
        loadItems([neededDyes[dye]])
        Client.waitTick()
        dyePixel(inv, positions[dyes[info][0]], neededDyes[dye])
      }
      end = false;
    }
  }
  dyes = getMapState(packet, dyesJson, false);
  neededDyes = getNeededDyes(dyes);
}


AntiAfk.getCtx().closeContext();
const endingTime = Time.time();
Chat.log("Art done in: " + ((endingTime - startingTime)/1000) + "s");




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