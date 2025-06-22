
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
       // Modifica los campos de estado del pico
   public void modificarPico(Pico pico) {
        String sql = """
                UPDATE Picos SET
                    localizacion = ?,
                    nombrePico = ?,
                    codigo_pico = ?,
                    abierto = ?,
                    altura = ?,
                    cambio_trekking = ?,
                    sin_aprobacion = ?,
                    año_de_cambio = ?,
                    estado = ?,
                    id_host = ?,
                    id_restricciones = ?
                WHERE id = ?""";

        try (Connection conn = DBConnection.getConnection();PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, pico.getLocalizacion());
            stmt.setString(2, pico.getNombrePico());
            stmt.setInt(3, pico.getId());
            stmt.setBoolean(4, pico.isAbierto());
            stmt.setFloat(5, pico.getAltura());
            stmt.setBoolean(6, pico.isCambio_trekking());
            stmt.setBoolean(7, pico.isSin_aprobacion());
            stmt.setInt(8, pico.getAño_de_cambio());
            stmt.setString(9, pico.getEstado());
            stmt.setInt(10, pico.getHost());
            stmt.setInt(11, pico.getRestricciones());
            stmt.setInt(12, pico.getId()); // importante que tengas `id` en la clase Pico PARA VERIFICAR EL ID ES ESTE

            int rows = stmt.executeUpdate();
            if (rows > 0) {
                System.out.println("Pico actualizado correctamente.");
            } else {
                System.out.println("No se encontró un pico con ese ID.");
            }

        } catch (SQLException e) {
            System.err.println("Error al modificar el pico: " + e.getMessage());
        }
    }
}

