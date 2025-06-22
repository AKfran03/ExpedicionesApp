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
}
