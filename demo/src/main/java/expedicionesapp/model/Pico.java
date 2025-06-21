/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package expedicionesapp.model;

/**
 *
 * @author Ramiro
 */
public class Pico {
     private String localizacion;
    private String nombrePico;
    private String codigo_pico;
    private String abierto;//si o no
    private float altura;
    private String cambio_trekking;//si o no
    private String sin_aprobacion;//si o no
    private String año_de_cambio;
    private String estado;//Escalado sin escalar
    private int id_host;//
    private int id_restricciones;

    public Pico(String localizacion, String nombrePico, String codigo_pico, String abierto, float altura, String cambio_trekking, String sin_aprobacion, String año_de_cambio, String estado, int id_host, int id_restricciones) {
        this.localizacion = localizacion;
        this.nombrePico = nombrePico;
        this.codigo_pico = codigo_pico;
        this.abierto = abierto;
        this.altura = altura;
        this.cambio_trekking = cambio_trekking;
        this.sin_aprobacion = sin_aprobacion;
        this.año_de_cambio = año_de_cambio;
        this.estado = estado;
        this.id_host = id_host;
        this.id_restricciones = id_restricciones;
    }
    

    public String getLocalizacion() {
        return localizacion;
    }

    public void setLocalizacion(String localizacion) {
        this.localizacion = localizacion;
    }

    public String getNombrePico() {
        return nombrePico;
    }

    public void setNombrePico(String nombrePico) {
        this.nombrePico = nombrePico;
    }

    public String getCodigo_pico() {
        return codigo_pico;
    }

    public void setCodigo_pico(String codigo_pico) {
        this.codigo_pico = codigo_pico;
    }

    public String getAbierto() {
        return abierto;
    }

    public void setAbierto(String abierto) {
        this.abierto = abierto;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public String getCambio_trekking() {
        return cambio_trekking;
    }

    public void setCambio_trekking(String cambio_trekking) {
        this.cambio_trekking = cambio_trekking;
    }

    public String getSin_aprobacion() {
        return sin_aprobacion;
    }

    public void setSin_aprobacion(String sin_aprobacion) {
        this.sin_aprobacion = sin_aprobacion;
    }

    public String getAño_de_cambio() {
        return año_de_cambio;
    }

    public void setAño_de_cambio(String año_de_cambio) {
        this.año_de_cambio = año_de_cambio;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public int getId_host() {
        return id_host;
    }

    public void setId_host(int id_host) {
        this.id_host = id_host;
    }

    public int getId_restricciones() {
        return id_restricciones;
    }

    public void setId_restricciones(int id_restricciones) {
        this.id_restricciones = id_restricciones;
    }
    
    
}
