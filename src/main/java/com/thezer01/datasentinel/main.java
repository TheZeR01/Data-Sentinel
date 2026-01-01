package com.thezer01.datasentinel;

import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerMoveEvent;
import org.bukkit.plugin.java.JavaPlugin;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class main extends JavaPlugin implements Listener {

    private File dataFolder;

    @Override
    public void onEnable() {
        getLogger().info("Data-sentinel: Analizando...");
        getServer().getPluginManager().registerEvents(this, this);

        // Crear carpeta para el registro/Dataset
        dataFolder = new File(getDataFolder(), "dataset");
        if (!dataFolder.exists()) dataFolder.mkdirs();
    }

    @Override
    public void onDisable() {
        getLogger().info("Data-sentinel: Guardando buffers y apagando.");
    }

    @EventHandler
    public void onPlayerMove(PlayerMoveEvent event) {

        long timestamp = System.currentTimeMillis();
        String playerUUID = event.getPlayer().getUniqueId().toString();

        // Datos Crudos para procesar (recoleccion para el dataset)
        double toX = event.getTo().getX();
        double toY = event.getTo().getY();
        double toZ = event.getTo().getZ();
        float toPitch = event.getTo().getPitch();
        float toYaw = event.getTo().getYaw();

        // Datos para Diferenciar
        double fromX = event.getFrom().getX();
        double fromY = event.getFrom().getY();
        double fromZ = event.getFrom().getZ();

        double deltaX = toX - fromX;
        double deltaY = toY - fromY; // Importante detector saltos/vuelo
        double deltaZ = toZ - fromZ;

        // Velocidad angular (Delta Pitch/Yaw, datos del movimiento del Mouse)
        float deltaPitch = toPitch - event.getFrom().getPitch();
        float deltaYaw = toYaw - event.getFrom().getYaw();

        // CSV
        logData(playerUUID, timestamp, deltaX, deltaY, deltaZ, deltaPitch, deltaYaw);
    }

    private void logData(String uuid, long time, double dX, double dY, double dZ, float dP, float dYw) {
        /*   //////////////
             ///  BETA! ///
             //////////////

           Trabajo en produccion, aqui el evento debe de ser asincrono para no producir caidas en servidor (Si lo olvido me mato)

         */
        try (PrintWriter writer = new PrintWriter(new FileWriter(new File(dataFolder, uuid + ".csv"), true))) {
            // Estructura: Timestamp, dX, dY, dZ, dPitch, dYaw
            writer.println(time + "," + String.format("%.4f", dX) + "," + String.format("%.4f", dY) + "," +
                    String.format("%.4f", dZ) + "," + String.format("%.4f", dP) + "," + String.format("%.4f", dYw));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
