package expedicionesapp.model;

public class Pico {
    private String localizacion;
    private String nombrePico;
    private int id;
    private boolean abierto;//si o no
    private float altura;
    private boolean cambio_trekking;//si o no
    private boolean sin_aprobacion;//si o no
    private int año_de_cambio;
    private String estado;//Escalado sin escalar
    private int host;//
    private int restricciones;

    public Pico(String localizacion, String nombrePico, int id, boolean abierto, float altura, boolean cambio_trekking, boolean sin_aprobacion, int año_de_cambio, String estado, int host, int restricciones) {
        this.localizacion = localizacion;
        this.nombrePico = nombrePico;
        this.id = id;
        this.abierto = abierto;
        this.altura = altura;
        this.cambio_trekking = cambio_trekking;
        this.sin_aprobacion = sin_aprobacion;
        this.año_de_cambio = año_de_cambio;
        this.estado = estado;
        this.host = host;
        this.restricciones = restricciones;
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

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getHost() {
        return host;
    }

    public void setHost(int host) {
        this.host = host;
    }

    public int getRestricciones() {
        return restricciones;
    }

    public void setRestricciones(int restricciones) {
        this.restricciones = restricciones;
    }



    public boolean isAbierto() {
        return abierto;
    }

    public void setAbierto(boolean abierto) {
        this.abierto = abierto;
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public boolean isCambio_trekking() {
        return cambio_trekking;
    }

    public void setCambio_trekking(boolean cambio_trekking) {
        this.cambio_trekking = cambio_trekking;
    }

    public boolean isSin_aprobacion() {
        return sin_aprobacion;
    }

    public void setSin_aprobacion(boolean sin_aprobacion) {
        this.sin_aprobacion = sin_aprobacion;
    }

    public int getAño_de_cambio() {
        return año_de_cambio;
    }

    public void setAño_de_cambio(int año_de_cambio) {
        this.año_de_cambio = año_de_cambio;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    } 
}
