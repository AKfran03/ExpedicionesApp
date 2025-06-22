
package expedicionesapp.model;

public class Miembros {
    private int id_miembro;
    private String nacionalidad;
    private String nombre;
    private String apellido;
    private String sexo;
    private boolean es_lider;
    private boolean es_staff;
    private int ano_nacimiento;
    private boolean fallecido;

    public Miembros(int id_miembro, String nacionalidad, String nombre, String apellido, String sexo, boolean es_lider, boolean es_staff, int ano_nacimiento, boolean fallecido) {
        this.id_miembro = id_miembro;
        this.nacionalidad = nacionalidad;
        this.nombre = nombre;
        this.apellido = apellido;
        this.sexo = sexo;
        this.es_lider = es_lider;
        this.es_staff = es_staff;
        this.ano_nacimiento = ano_nacimiento;
        this.fallecido = fallecido;
    }
    

    public boolean isEs_lider() {
        return es_lider;
    }

    public void setEs_lider(boolean es_lider) {
        this.es_lider = es_lider;
    }

    public boolean isEs_staff() {
        return es_staff;
    }

    public void setEs_staff(boolean es_staff) {
        this.es_staff = es_staff;
    }

    public boolean isFallecido() {
        return fallecido;
    }

    public void setFallecido(boolean fallecido) {
        this.fallecido = fallecido;
    }
    


    public int getId_miembro() {
        return id_miembro;
    }

    public void setId_miembro(int id_miembro) {
        this.id_miembro = id_miembro;
    }

    public String getNacionalidad() {
        return nacionalidad;
    }

    public void setNacionalidad(String nacionalidad) {
        this.nacionalidad = nacionalidad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }


    public int getAno_nacimiento() {
        return ano_nacimiento;
    }

    public void setAno_nacimiento(int ano_nacimiento) {
        this.ano_nacimiento = ano_nacimiento;
    }


    
}
