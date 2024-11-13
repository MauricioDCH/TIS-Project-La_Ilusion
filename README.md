# TIS-Project-La_Ilusión
This project is created in order to meet the requirements of the subject Special Topics in Software Engineering and additionally begin the execution of the development of the website of the company La Ilusión Pisos y Enchapes

## 1. Autores
---
[<img src="https://avatars.githubusercontent.com/u/81777898?s=400&u=2eeba9c363f9c474c7fb419ef36562e2d2b6b866&v=4" width=115><br><sub>Mauricio David Correa Hernández.</sub>](https://github.com/MauricioDCH) | [<img src="https://avatars.githubusercontent.com/u/88986744?v=4" width=115><br><sub>Camilo Ortegon Saugter.</sub>](https://github.com/cortegons) |  
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |

# Run the project.

```bash
python manage.py runserver
```

# Main route of the project.
```bash
http://0.0.0.0:8000/
```
To pull request

Usuario: mdcorreah@eafit.edu.co

Contraseña: LIMauricio159!!!

Ya que ha estado borrándose la bd.

# Para migrar la base de datos que estaba en local.

```
python manage.py dumpdata --natural-primary --natural-foreign --indent 4 > data.json
```

```
docker compose exec web python manage.py migrate
```

```
docker compose exec web python manage.py loaddata data.json
```