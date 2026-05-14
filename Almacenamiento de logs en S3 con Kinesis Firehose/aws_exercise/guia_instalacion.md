# Guía: Anaconda + Jupyter + PySpark en EC2 (2025)

## Versiones recomendadas

| Componente | Versión |
|---|---|
| AMI | Ubuntu 24.04 LTS (Jammy Jellyfish) |
| Anaconda | Última (Python 3.11) |
| Java | OpenJDK 11 |
| Spark | 3.5.5 con Hadoop 3 |
| PySpark | 3.5.5 (vía pip) |

---

## 1. Lanzar la instancia EC2

En la consola de AWS:
- AMI: **Ubuntu Server 22.04 LTS**
- Tipo: `t3.medium` o superior (mínimo 4 GB RAM para Spark)
- **Security Group**: abre el puerto **8888** (TCP) solo si usarás acceso directo; no es necesario con túnel SSH
- Descarga tu `.pem` y ajusta permisos:

```bash
chmod 400 tu-clave.pem
```

---

## 2. Conectarse a la instancia

```bash
ssh -i "tu-clave.pem" ubuntu@<DNS-público-de-tu-instancia>
```

> El DNS público cambia cada vez que reinicias la instancia. Si necesitas una dirección fija, asigna una **IP elástica** en la consola de AWS.

---

## 3. Instalar Anaconda

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
bash Anaconda3-2024.10-1-Linux-x86_64.sh
source ~/.bashrc
```

Verifica:
```bash
conda --version
python --version  # debe mostrar 3.11.x
```

---

## 4. Instalar Java 11

```bash
sudo apt-get update
sudo apt-get install -y openjdk-11-jdk
java -version
```

---

## 5. Instalar Spark 3.5

```bash
wget https://archive.apache.org/dist/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz
tar -xzf spark-3.5.5-bin-hadoop3.tgz
mv spark-3.5.5-bin-hadoop3 ~/spark
```

Agregar al final de `~/.bashrc`:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export SPARK_HOME=~/spark
export PATH=$SPARK_HOME/bin:$PATH
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH
export PYSPARK_PYTHON=python3
```

Aplicar cambios:
```bash
source ~/.bashrc
```

---

## 6. Instalar PySpark

```bash
pip install pyspark==3.5.5
```

---

## 7. Configurar Jupyter

```bash
jupyter notebook --generate-config
```

Agregar al final de `~/.jupyter/jupyter_notebook_config.py`:

```python
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.token = ''
c.NotebookApp.password = ''
```

> Para usar JupyterLab (versión moderna recomendada): `pip install jupyterlab` y ejecutar con `jupyter lab`.

---

## 8. Iniciar Jupyter

```bash
jupyter notebook
# o con JupyterLab:
jupyter lab
```

---

## 9. Acceder desde tu navegador local

### Opción A: Túnel SSH (recomendada, sin abrir puertos)

Desde tu máquina local, en una terminal aparte:

```bash
ssh -i "tu-clave.pem" -L 8888:localhost:8888 ubuntu@<DNS-público> -N
```

Luego abre en tu navegador:
```
http://localhost:8888
```

### Opción B: Acceso directo por IP pública

Requiere tener el puerto 8888 abierto en el Security Group. Abre en tu navegador:
```
http://<DNS-público-de-tu-instancia>:8888
```

---

## 10. Verificar PySpark en un notebook

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("test") \
    .master("local[*]") \
    .getOrCreate()

print(spark.version)  # debe mostrar '3.5.5'
```

---

## 11. Al terminar: apagar la instancia

Para evitar costos innecesarios, detén la instancia desde la consola de AWS o con:

```bash
sudo shutdown -h now
```

---

## Notas

- Ubuntu 20.04 ya no tiene soporte estándar desde abril 2025; usa 22.04 o 24.04.
- El túnel SSH es la opción más segura para acceder a Jupyter.
- `master("local[*]")` usa todos los núcleos de la instancia; es suficiente para ejercicios introductorios sin necesidad de configurar un cluster.
- Los notebooks escritos para Spark 2.x son mayormente compatibles con Spark 3.5, pero revisa el uso de `DataFrame.toPandas()` y funciones SQL que cambiaron de comportamiento.
