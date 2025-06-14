package expedicionesapp;

import expedicionesapp.util.Conexion;

public class Main {
    public static void main(String[] args) {
        Conexion c = new Conexion();
        c.mostrarMiembros();
    }
}
/*
lo que necesitamos:
	id expedicion, id fecha, id accidente, id miembro, id pico, id resultado, id ruta, altitud, cupos, conteo mortalidad.

Como lo tenemos:
	id_expedicion,codigo_pico,Año,host,Temporada,nombre_Temporada,Pais,Lideres,Exito,motivo_terminacion,altitud,cupo,Muertes,Accidente,Ruta,Fecha,Dia_Mas_Alto

El orden a seguir para crear las bases de datos va a ser el siguente.

1-[dbo].[Fecha]
2-[dbo].[Accidente]
3-[dbo].[Nacionalidad] (para miembros.)
4-[dbo].[Miembros]
5-[dbo].[Host]
6-[dbo].[Localizacion]
7-[dbo].[Pico]
8-[dbo].[Motivo]
9-[dbo].[Resultado]
10-[dbo].[Ruta]
11-[dbo].[Expediciones]


1- Para fecha necesitamos:
	fecha será sacado de la tabla expediciones.
	fecha (date), año (int), temporada (int [verano = 2, otoño = 3, invierno = 4, primavera = 1, ya esta asi, no se pregunta.. xd]);
	Fecha,Año,Temporada
2- para Accidente

*/