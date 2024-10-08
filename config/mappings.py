"""
Diccionarios de Mapeo para Cursos y Predicciones

course_mapping:
    Este diccionario asocia códigos numéricos de cursos a nombres de cursos específicos. 
    Se utiliza para traducir los códigos de cursos en nombres legibles en la interfaz de usuario.
   
prediction_mapping:
    Este diccionario asocia códigos de predicción numéricos a categorías de predicción de estudiantes.
    Se utiliza para traducir los códigos de predicción en descripciones legibles como "Dropout", "Enrolled" o "Graduate".
"""

course_mapping = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)",
}

prediction_mapping = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
