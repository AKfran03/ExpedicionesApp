package expedicionesapp.dao;

import expedicionesapp.util.DBConnection;
import expedicionesapp.model.Miembros;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MiembrosDao {
     public void mostrarMiembroPorId(int id_miembro) {
        String sql = "SELECT * FROM Miembros WHERE id_miembro = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id_miembro);
            ResultSet rs = stmt.executeQuery(); 

            if (rs.next()) {
                System.out.println("ID: " + rs.getInt("id_miembro"));
                System.out.println("Nombre : " + rs.getString("nombre"));
                System.out.println("Apellido: " + rs.getString("apellido"));
                System.out.println("Nacionalidad: " + rs.getString("nacionalidad"));
                System.out.println("Sexo: " + rs.getString("sexo"));
                System.out.println("Es Lider: " + rs.getBoolean("es_lider"));
                System.out.println("Es Contratado: " + rs.getBoolean("es_staff"));
                System.out.println("Año de Nacimiento: " + rs.getInt("año_nacimiento"));
                System.out.println("Fallecido: " + rs.getBoolean("estado"));
            } else {
                System.out.println("No se encontro ningun pico con el ID " + id_miembro);
            }

        } catch (SQLException e) {
            System.err.println("Error al mostrar el pico: " + e.getMessage());
        }
    }
    public void InsertarMiembro(Miembros miembro){
         String sql = "INSERT INTO Miembros (id_miembro, nacionalidad, nombre, apellido, sexo, es_lider, es_staff, ano_nacimiento, fallecido)" + "VALUES (?,?,?,?,?,?,?,?,?)";
         try (Connection conn = DBConnection.getConnection();
         PreparedStatement stmt = conn.prepareStatement(sql)){
             stmt.setInt(1, miembro.getId_miembro());
             stmt.setString(2, miembro.getNacionalidad());
             stmt.setString(3, miembro.getNombre());
             stmt.setString(4, miembro.getApellido());
             stmt.setString(5, miembro.getSexo());
             stmt.setBoolean(6, miembro.isEs_lider());
             stmt.setBoolean(7, miembro.isEs_staff());
             stmt.setInt(8, miembro.getAno_nacimiento());
             stmt.setBoolean(9, miembro.isFallecido());
             stmt.executeUpdate();
             System.out.println("Miembro agregado correctamente");
        }catch (SQLExeption e){
             System.err.println("Error al insertar el miembro: " + e.getMessage());

         }

    }
}
