
package expedicionesapp.dao;
import expedicionesapp.util.DBConnection;
import expedicionesapp.model.Pico;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class PicoDao {
        // Muestra UN solo pico por su ID
    public void mostrarPicoPorId(int id_Pico) {
        String sql = "SELECT * FROM Pico WHERE id_Pico = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id_Pico);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                System.out.println("ID: " + rs.getInt("id"));
                System.out.println("Nombre del Pico: " + rs.getString("nombrePico"));
                System.out.println("Código: " + rs.getString("codigo_pico"));
                System.out.println("Abierto: " + rs.getString("abierto"));
                System.out.println("Altura: " + rs.getFloat("altura"));
                System.out.println("Cambio Trekking: " + rs.getString("cambio_trekking"));
                System.out.println("Sin Aprobación: " + rs.getString("sin_aprobacion"));
                System.out.println("Año de Cambio: " + rs.getString("año_de_cambio"));
                System.out.println("Estado: " + rs.getString("estado"));
                System.out.println("ID Host: " + rs.getInt("id_host"));
                System.out.println("ID Restricciones: " + rs.getInt("id_restricciones"));
            } else {
                System.out.println("No se encontro ningun pico con el ID " + id_Pico);
            }

        } catch (SQLException e) {
            System.err.println("Error al mostrar el pico: " + e.getMessage());
        }
    }
    
}
