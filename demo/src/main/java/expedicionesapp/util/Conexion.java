package expedicionesapp.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Conexion {
    private Connection conn;

    public Conexion() {
        conn = null;
        this.conectar();
    }

    public void conectar() {
        String url = "jdbc:sqlserver://206.189.237.186:14111;databaseName=Grupo6;user=tferreyra;password=Tomas44520!;encrypt=false";
        try {
            conn = DriverManager.getConnection(url);
            System.out.println("Se estableció la conexión con la base de datos.");
        } catch (SQLException e) {
            System.out.println("Error al conectar con la base de datos. Error: " + e.getMessage());
        }
    }

    public void mostrarMiembros() {
        ResultSet rs;
        try {
            Statement statement = this.conn.createStatement();
            rs = statement.executeQuery("SELECT * FROM dbo.Miembros");
            int columnas = rs.getMetaData().getColumnCount();
            while (rs.next()) {
                for (int i = 1; i <= columnas; i++) {
                    System.out.print(rs.getString(i) + " ");
                }
                System.out.println();
            }
        } catch (SQLException e) {
            System.out.println("Error al consultar la base de datos. Error: " + e.getMessage());
        }
    }

    public Connection getConexion() {
        return conn;
    }
}
