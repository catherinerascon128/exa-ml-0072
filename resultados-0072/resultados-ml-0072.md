# Reporte de Análisis de Datos - Pandas

`catherine eileen huerta rascon Machine Learning pandas, NC 0072`

## 1. DataFrame Convertido
```text
       Festival  Artistas  Dias
0    Cervantino       150    25
1          Jazz        40     5
2          Cine        80    10
3  Gastronómico        60     7
4      Cultural       100    15
5       Musical        75     3
```

## 2.1 Primeras Filas (head)
```text
     Festival  Artistas  Dias
0  Cervantino       150    25
1        Jazz        40     5
```

## 2.2 Últimas Filas (tail)
```text
   Festival  Artistas  Dias
4  Cultural       100    15
5   Musical        75     3
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Festival      str
Artistas    int64
Dias        int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Festival  6 non-null      str  
 1   Artistas  6 non-null      int64
 2   Dias      6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Artistas'
```text
count      6.000000
mean      84.166667
std       38.002193
min       40.000000
25%       63.750000
50%       77.500000
75%       95.000000
max      150.000000
Name: Artistas, dtype: float64
```

## 4. Ordenar Ascendente por Artistas
```text
       Festival  Artistas  Dias
1          Jazz        40     5
3  Gastronómico        60     7
5       Musical        75     3
2          Cine        80    10
4      Cultural       100    15
0    Cervantino       150    25
```

## 5. Ordenar Descendente por Dias
```text
       Festival  Artistas  Dias
0    Cervantino       150    25
4      Cultural       100    15
2          Cine        80    10
3  Gastronómico        60     7
1          Jazz        40     5
5       Musical        75     3
```

`catherine eileen huerta rascon Machine Learning pandas, NC 0072`