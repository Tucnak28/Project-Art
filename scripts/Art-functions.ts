const lookupTable = {"4":"grass2","5":"grass1","6":"grass0","7":"grass3","8":"pumpkin_seeds2","9":"pumpkin_seeds1","10":"pumpkin_seeds0","11":"pumpkin_seeds3","12":"cobweb2","13":"cobweb1","14":"cobweb0","15":"cobweb3","16":"red_dye2","17":"red_dye1","18":"red_dye0","19":"red_dye3","20":"ice2","21":"ice1","22":"ice0","23":"ice3","24":"light_gray_dye2","25":"light_gray_dye1","26":"light_gray_dye0","27":"light_gray_dye3","28":"oak_leaves2","29":"oak_leaves1","30":"oak_leaves0","31":"oak_leaves3","32":"snow2","33":"snow1","34":"snow0","35":"snow3","36":"gray_dye2","37":"gray_dye1","38":"gray_dye0","39":"gray_dye3","40":"melon_seeds2","41":"melon_seeds1","42":"melon_seeds0","43":"melon_seeds3","44":"ghast_tear2","45":"ghast_tear1","46":"ghast_tear0","47":"ghast_tear3","48":"lapis_block2","49":"lapis_block1","50":"lapis_block0","51":"lapis_block3","52":"dark_oak_log2","53":"dark_oak_log1","54":"dark_oak_log0","55":"dark_oak_log3","56":"bone_meal2","57":"bone_meal1","58":"bone_meal0","59":"bone_meal3","60":"orange_dye2","61":"orange_dye1","62":"orange_dye0","63":"orange_dye3","64":"magenta_dye2","65":"magenta_dye1","66":"magenta_dye0","67":"magenta_dye3","68":"light_blue_dye2","69":"light_blue_dye1","70":"light_blue_dye0","71":"light_blue_dye3","72":"yellow_dye2","73":"yellow_dye1","74":"yellow_dye0","75":"yellow_dye3","76":"lime_dye2","77":"lime_dye1","78":"lime_dye0","79":"lime_dye3","80":"pink_dye2","81":"pink_dye1","82":"pink_dye0","83":"pink_dye3","84":"flint2","85":"flint1","86":"flint0","87":"flint3","88":"gunpowder2","89":"gunpowder1","90":"gunpowder0","91":"gunpowder3","92":"cyan_dye2","93":"cyan_dye1","94":"cyan_dye0","95":"cyan_dye3","96":"purple_dye2","97":"purple_dye1","98":"purple_dye0","99":"purple_dye3","100":"lapis_lazuli2","101":"lapis_lazuli1","102":"lapis_lazuli0","103":"lapis_lazuli3","104":"cocoa_beans2","105":"cocoa_beans1","106":"cocoa_beans0","107":"cocoa_beans3","108":"green_dye2","109":"green_dye1","110":"green_dye0","111":"green_dye3","112":"brick2","113":"brick1","114":"brick0","115":"brick3","116":"ink_sac2","117":"ink_sac1","118":"ink_sac0","119":"ink_sac3","120":"gold_nugget2","121":"gold_nugget1","122":"gold_nugget0","123":"gold_nugget3","124":"prismarine_crystals2","125":"prismarine_crystals1","126":"prismarine_crystals0","127":"prismarine_crystals3","-122":"emerald0","-123":"emerald1","-124":"emerald2","-121":"emerald3","-70":"chorus_fruit0","-71":"chorus_fruit1","-72":"chorus_fruit2","-69":"chorus_fruit3","-54":"apple0","-55":"apple1","-56":"apple2","-53":"apple3","-94":"glowstone_dust0","-95":"glowstone_dust1","-96":"glowstone_dust2","-93":"glowstone_dust3","-58":"poisonous_potato0","-59":"poisonous_potato1","-60":"poisonous_potato2","-57":"poisonous_potato3","-106":"magma_cream0","-107":"magma_cream1","-108":"magma_cream2","-105":"magma_cream3","-114":"nether_wart0","-115":"nether_wart1","-116":"nether_wart2","-113":"nether_wart3","-98":"mycelium0","-99":"mycelium1","-100":"mycelium2","-97":"mycelium3","-66":"purpur_block0","-67":"purpur_block1","-68":"purpur_block2","-65":"purpur_block3","-126":"lapis_ore0","-127":"lapis_ore1","-128":"lapis_ore2","-125":"lapis_ore3","-110":"egg0","-111":"egg1","-112":"egg2","-109":"egg3","-74":"iron_nugget0","-75":"iron_nugget1","-76":"iron_nugget2","-73":"iron_nugget3","-118":"birch_wood0","-119":"birch_wood1","-120":"birch_wood2","-117":"birch_wood3","-102":"beetroot0","-103":"beetroot1","-104":"beetroot2","-101":"beetroot3","-90":"slime_ball0","-91":"slime_ball1","-92":"slime_ball2","-89":"slime_ball3","-86":"spider_eye0","-87":"spider_eye1","-88":"spider_eye2","-85":"spider_eye3","-82":"soul_sand0","-83":"soul_sand1","-84":"soul_sand2","-81":"soul_sand3","-78":"brown_mushroom0","-79":"brown_mushroom1","-80":"brown_mushroom2","-77":"brown_mushroom3","-46":"crimson_nylium0","-47":"crimson_nylium1","-48":"crimson_nylium2","-45":"crimson_nylium3","-34":"warped_nylium0","-35":"warped_nylium1","-36":"warped_nylium2","-33":"warped_nylium3","-26":"warped_hyphae0","-27":"warped_hyphae1","-28":"warped_hyphae2","-25":"warped_hyphae3","-18":"cobbled_deepslate0","-19":"cobbled_deepslate1","-20":"cobbled_deepslate2","-17":"cobbled_deepslate3","-10":"glow_lichen0","-11":"glow_lichen1","-12":"glow_lichen2","-9":"glow_lichen3","-14":"raw_iron0","-15":"raw_iron1","-16":"raw_iron2","-13":"raw_iron3","-62":"podzol0","-63":"podzol1","-64":"podzol2","-61":"podzol3","-50":"charcoal0","-51":"charcoal1","-52":"charcoal2","-49":"charcoal3","-22":"warped_wart_block0","-23":"warped_wart_block1","-24":"warped_wart_block2","-21":"warped_wart_block3","-42":"crimson_stem0","-43":"crimson_stem1","-44":"crimson_stem2","-41":"crimson_stem3","-38":"crimson_hyphae0","-39":"crimson_hyphae1","-40":"crimson_hyphae2","-37":"crimson_hyphae3","-30":"warped_stem0","-31":"warped_stem1","-32":"warped_stem2","-29":"warped_stem3"}

function dyeBucket(inv, item) {
    // find the slots for the required items
    const mostUsedSlot = inv.findItem(item.slice(0, -1))[0] // the most-used item (e.g. bone meal)
    const bucketSlot = inv.findItem("minecraft:bucket")[0] // bucket slot
    const featherSlot = inv.findItem("minecraft:feather")[0] // feather slot
    const coalSlot =  inv.findItem("minecraft:coal")[0] // coal slot
  
    // make sure we have all required items, otherwise return null
    if (mostUsedSlot != null && bucketSlot != null && featherSlot != null && coalSlot != null) {   // Swap items as needed
      if(mostUsedSlot != 45) {
        inv.swap(mostUsedSlot, 45);
      }
      if(bucketSlot != 44) {
        inv.swap(bucketSlot, 44);
      }
      if(coalSlot != 43) {
        inv.swap(coalSlot, 43);
      }
      if(featherSlot != 42) {
        inv.swap(featherSlot, 42);
      }
    } else {
      return null;
    }
  
    // attack with bucket, selecting correct slot,
    // looking in the right direction and swapping back items
    const player = Player.getPlayer();
    smoothLook(Player.getPlayer(), 89, 1, 6, 1); // turn to the right direction
    inv.setSelectedHotbarSlotIndex(8);
    Client.waitTick(8)
    player.attack();
    Client.waitTick(8)
    inv.swap(45, mostUsedSlot); // Swap items back
    Client.waitTick(8)
    switch(item.charAt(item.length - 1)) {
      // dye item to be used
      case "0":
        inv.swap(42, 45);
        Client.waitTick(8)
        player.attack();
        inv.swap(45, 42);
        Client.waitTick(8)
        break;
      case "1":
        break;
      case "2":
        inv.swap(43, 45);
        Client.waitTick(8)
        player.attack();
        inv.swap(45, 43);
        Client.waitTick(8)
        break;
      case "3":
        inv.swap(43, 45);
        Client.waitTick(8)
        player.attack();
        Client.waitTick(8)
        player.attack();
        Client.waitTick(8)
        inv.swap(45, 43);
        Client.waitTick(8)
        break;
      default:
        Chat.log("Unknown dye item: " + item);
        break;
    }
}
  
  
function loadItems(neededDyes) { 
    Chat.say("/backpack");
    JsMacros.waitForEvent("OpenScreen");
    Client.waitTick()
    let inv = Player.openInventory();
    for(let k = 0; k <= 2; k++) {
    for(let i = 0; i <= 89; i++) {
        const itemID = inv.getSlot(i).getItemID();
        if(neededDyes.includes(itemID)) {
        const targetSlot = 89 - neededDyes.findIndex(id => id === itemID);
        if(targetSlot < 54 || targetSlot == i) continue;
        inv.swap(i, targetSlot);
        Time.sleep(1);
        }
    };
    }
    inv.close();
    inv.sync();
    Client.waitTick();
}

function smoothLook(player, goalYaw, goalPitch, TIME, TIME_INTERVAL) {
    var yawDifference = goalYaw - player.getYaw()
    var pitchDifference = goalPitch - player.getPitch()

    const STEPS = TIME / TIME_INTERVAL
    for(let i = 0; i < STEPS; i ++) {
        player.lookAt(player.getYaw() + yawDifference / STEPS, player.getPitch() + pitchDifference / STEPS)
        Client.waitTick(TIME_INTERVAL)
    }
}

const rows = [
    [9, 10, 11, 12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23, 24, 25, 26],
    [27, 28, 29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42, 43, 44]
]

function findRow(slot) {
    for(let i = 0; i < rows.length; i++) {
    if(rows[i].includes(slot)) return i
    }
    return -1;
}

    
function findHotbar(map, item) {
    for (let i = 0; i <= 8; i++) {
    if(inv.getSlot(map.hotbar[i]).getItemID() == item) {
        return i
    }
    }
    return -1;
}

function dyePixel(inv, position, dye) {
    let hotbarSlot = findHotbar(inv.getMap(), dye);
    if(hotbarSlot == -1) {
    
    const row = rows[findRow(inv.findItem(dye)[0])];
    if(!row) {
        return -1;
    }

    for(let i = 0; i < row.length; i++) {
        inv.swapHotbar(row[i], i);
    }
    Client.waitTick();
    hotbarSlot = findHotbar(inv.getMap(), dye);
    }

    if(hotbarSlot != inv.getSelectedHotbarSlotIndex()) {
    inv.setSelectedHotbarSlotIndex(hotbarSlot);
    }

    const [yaw, pitch] = position;
    ////Chat.log(yaw.toFixed(0) + ", " + pitch.toFixed(0) + ": " + dye);
    smoothLook(Player.getPlayer(), yaw, pitch, 4, 1); //200, 50
    //Client.waitTick(5);
    Player.getPlayer().attack();
    return 1
}


function getMapState(colorsObj, dyesJson, first) {
    const colorsArray = [];

    for (let i = 0; i < colorsObj.length; i = i + 128) {
        let rowArray = [];
        for (let j = i; j < i + 128; j = j + 4) {
            let pixelArray = colorsObj.slice(j, j + 4);
            let pixelColor = pixelArray[0];
            if (pixelArray.every(val => val == pixelColor)) {
                rowArray.push(pixelColor);
            } else {
                rowArray.push(-1); // indicates that this 4x4 block is not uniform
            }
        }
        colorsArray.push(rowArray);
    }
    const actualColors = colorsArray.filter((row, index) => index % 4 === 0);
    /*
    let numRows = actualColors.length;
    let numColumns = actualColors[0].length;
    let numElements = numRows * numColumns;
    
    Chat.log("Number of rows: " + numRows);
    Chat.log("Number of columns: " + numColumns);
    Chat.log("Size of colorsArray: " + numElements);*/

    
    const translatedArray = actualColors.map(subArray => {
    return subArray.map(num => {
        return lookupTable[num.toString()];
    });
    });

    let array1D = translatedArray.flat();
    if(first && array1D.every(val => val === array1D[0])) return false;

    let errorArray = [];
    for (const key in dyesJson) {
        if(array1D[key - 1] == dyesJson[key]) continue;
        const index = parseInt(key);
        let intDye = dyesJson[key].slice(0, -1);
        const curDye = array1D[key - 1].slice(0, -1); 
        const intShade = parseInt(dyesJson[key].charAt(dyesJson[key].length - 1));
        const curShade = parseInt(array1D[key - 1].charAt(array1D[key - 1].length - 1));
        const shadeCorrection = curShade - intShade;
        if(intDye == curDye) {
        
        if(shadeCorrection < 0) {intDye = "coal"}
        else if(shadeCorrection > 0) {intDye = "feather"} 
        else {
            intDye = "done"
        }
        }
        errorArray.push([index, [intDye, shadeCorrection]]);
    }
    return errorArray;
}

function getCurrentPacket() {
    World.getEntities().forEach(entity => {
    if(entity.getName().getString() == "Easel") {
        const inv = Player.openInventory()
        Client.waitTick(5);
        inv.swap(inv.getSelectedHotbarSlotIndex() + 36, 45);
        Client.waitTick(5);
        Player.getPlayer().interactEntity(entity, false);
        Client.waitTick(5);
        inv.swap(inv.getSelectedHotbarSlotIndex() + 36, 45);
        Client.waitTick(5);
    }
    });
}

function getMostUsed(dyesJson) {
    const values = Object.values(dyesJson);

    // Create an object to store the counts of each value
    const valueCounts = {};

    // Count the occurrences of each value
    values.forEach((value) => { 
    if (value in valueCounts) {
        valueCounts[value]++;
    } else {
        valueCounts[value] = 1;
    }
    });

    // Get an array of the entries in the valueCounts object
    const entries = Object.entries(valueCounts);

    // Sort the entries based on the count of each value
    entries.sort((a, b) => b[1] - a[1]);

    const mostUsedValues = entries.map((entry) => entry[0]).map(x => "minecraft:" + x);

    return mostUsedValues[0]
}

function getNeededDyes(dyes) {
    let dyeValues = [];
    for (let i = 0; i < dyes.length; i++) {
        dyeValues.push(dyes[i][1]);
    }

    const sortedDyeValues = dyeValues.reduce((acc, curr) => {
    const index = acc.findIndex(element => element[0] === curr[0] && element[1] === curr[1]);
    if (index === -1) {
        acc.push([curr[0], curr[1], 1]);
    } else {
        acc[index][2] += 1;
    }
    return acc;
    }, []).sort((a, b) => b[2] - a[2]).map(dye => [dye[0], dye[1]]);

    //array that have only one of every dye
    const neededDyes = sortedDyeValues.reduce(function(acc, curr) {
    const foundItem = acc.find(i => i === curr[0]);
    if (!foundItem) {
        acc.push(curr[0])
    }
    return acc;
    }, []).map(x => "minecraft:" + x);

    return neededDyes;
}

function saveImage(name) {
    const player = Player.getPlayer();
    const inv = Player.openInventory()
    Client.waitTick(15);
	Chat.say(`/art save ${name}`)
    Client.waitTick(20);
    smoothLook(player, 89, 1, 6, 1)
    Client.waitTick(10);
    inv.swap(inv.getSelectedHotbarSlotIndex() + 36, 45);
    Client.waitTick(5);
    player.interact();
    Client.waitTick(10);
    player.interact();
    Client.waitTick(5);
    inv.swap(inv.getSelectedHotbarSlotIndex() + 36, 45);
	Client.waitTick(10);
}

module.exports = { dyeBucket, loadItems, dyePixel, getMapState, getCurrentPacket, getMostUsed, getNeededDyes, saveImage };