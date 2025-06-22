package expedicionesapp.model;

public class Expediciones {
    private int id_expedicion;
    private int id_accidente;
    private int id_pico;
    private float altitud;
    private int cupo;
    private int conteo_mortalidad;
    private String fecha;
    private String resultado;
    private String motivo;
    private String ruta;

    public Expediciones(int id_expedicion, int id_accidente, int id_pico, float altitud, int cupo, int conteo_mortalidad, String fecha, String resultado, String motivo, String ruta) {
        this.id_expedicion = id_expedicion;
        this.id_accidente = id_accidente;
        this.id_pico = id_pico;
        this.altitud = altitud;
        this.cupo = cupo;
        this.conteo_mortalidad = conteo_mortalidad;
        this.fecha = fecha;
        this.resultado = resultado;
        this.motivo = motivo;
        this.ruta = ruta;
    }

    public int getId_expedicion() {
        return id_expedicion;
    }

    public void setId_expedicion(int id_expedicion) {
        this.id_expedicion = id_expedicion;
    }

    public int getId_accidente() {
        return id_accidente;
    }

    public void setId_accidente(int id_accidente) {
        this.id_accidente = id_accidente;
    }

    public int getId_pico() {
        return id_pico;
    }

    public void setId_pico(int id_pico) {
        this.id_pico = id_pico;
    }

    public float getAltitud() {
        return altitud;
    }

    public void setAltitud(float altitud) {
        this.altitud = altitud;
    }

    public int getCupo() {
        return cupo;
    }

    public void setCupo(int cupo) {
        this.cupo = cupo;
    }

    public int getConteo_mortalidad() {
        return conteo_mortalidad;
    }

    public void setConteo_mortalidad(int conteo_mortalidad) {
        this.conteo_mortalidad = conteo_mortalidad;
    }

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public String getResultado() {
        return resultado;
    }

    public void setResultado(String resultado) {
        this.resultado = resultado;
    }

    public String getMotivo() {
        return motivo;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }

    public String getRuta() {
        return ruta;
    }

    public void setRuta(String ruta) {
        this.ruta = ruta;
    }
    
    
    
}
