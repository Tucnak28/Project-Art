/*const types = [];

const listener = JsMacros.on("SendPacket", JavaWrapper.methodToJava(event => {

    if(!types.includes(event.type)){
        types.push(event.type);
        FS.open("packets.json").write(JSON.stringify(types));
        Chat.log(event.type);
    }
}));*/






/*for (const key in ChatMessageC2SPacket) {
    Chat.log(key);
}*/
/*for (const key in Client.createPacketByteBuffer()) {
    Chat.log(key);
}*/


const PlayerInteractEntityC2SPacket = Java.type("net.minecraft.class_2824");
const PacketByteBuf = Java.type("net.minecraft.class_2540");
let entityId = Reflection.getDeclaredField(PlayerInteractEntityC2SPacket, "field_12870");

let bufferConstructor = Client.createPacketByteBuffer()

entityId.setAccessible(true);
let id;

const listener = JsMacros.on("SendPacket", JavaWrapper.methodToJava(event => {
    if(event.type !== "PlayerInteractEntityC2SPacket") return;
    id = entityId.getInt(event.packet);
    Chat.log(id);
}));

Player.getPlayer().attack();
Time.sleep(1000);

bufferConstructor.writeVarInt(id);
bufferConstructor.writeVarInt(1);
bufferConstructor.writeBoolean(false);

let buffer = new PacketByteBuf(bufferConstructor);

const packet = new PlayerInteractEntityC2SPacket(buffer);

while(1) {
    Client.sendPacket(packet);
    Time.sleep(150);
}
