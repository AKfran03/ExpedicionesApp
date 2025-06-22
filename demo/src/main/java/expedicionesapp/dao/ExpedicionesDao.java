
package expedicionesapp.dao;
import expedicionesapp.util.DBConnection;
import expedicionesapp.model.Expediciones;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ExpedicionesDao {
     public void mostrarExpedicionPorId(int id_Expedicion) {
        String sql = "SELECT * FROM Expedicion WHERE id_Expedicion = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id_Expedicion);
            ResultSet rs = stmt.executeQuery();

            if (rs.next()) {
                System.out.println("Expedicion: " + rs.getInt("id"));
                System.out.println("ID_Pico: " + rs.getInt("id_Pico"));
                System.out.println("ID_Accidente: " + rs.getInt("id_accidente"));
                System.out.println("Altitud: " + rs.getFloat("altitud"));
                System.out.println("Cant.Miembros: " + rs.getInt("cupo"));
                System.out.println("Conteo Mortalidad: " + rs.getInt("conteo_mortalidad"));
                System.out.println("Fecha: " + rs.getString("Fecha"));
                System.out.println("Resultado: " + rs.getString("resultado"));
                System.out.println("Motivo: " + rs.getString("motivo"));
                System.out.println("Ruta: " + rs.getString("ruta"));
            } else {
                System.out.println("No se encontro ninguna expedicion con el ID " + id_Expedicion);
            }

        } catch (SQLException e) {
            System.err.println("Error al mostrar el pico: " + e.getMessage());
        }
   }
}
