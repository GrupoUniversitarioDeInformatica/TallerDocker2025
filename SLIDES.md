%%

> [!TIP]
> This Markdown format won't look pretty in GitHub. It is thought to be used with Obsidian Slides plugin to work as a presentation.

En este taller veremos qué es Docker, por qué es útil y necesario tanto en el desarrollo de software como en la administración de sistemas y un ejemplo práctico desde 0 donde aprenderéis a correr vuestro propio servidor de Overleaf dedicado.

%%

## Contenidos

- Introducción a Docker y Docker Compose
  - ¿Qué es Docker?
  - ¿Cómo creo una imagen de Docker?
  - ¿Qué es Docker Compose?
---
- Contexto en el desarrollo de software:
  - ¿Cómo containerizar una app escrita en Python para despliegue a producción? (ejemplo práctico con una app en Python)
  - ¿Cómo usar Docker DURANTE el desarrollo de software?

- Contexto en la administración de sistemas
  - ¿Cómo usar Docker para monitorización de un sistema / app? (ejemplo práctico con Grafana + Prometheus)

---

- BONUS (si nos da tiempo)
  - Overleaf dedicado corriendo como contenedor de Docker
  - Alternativas a Docker
  - Testcontainers
  - Casos de uso real de Docker

---
## Introducción a Docker y Docker Compose

- ¿Qué es Docker?
- ¿Cómo creo una imagen de Docker?
- ¿Qué es Docker Compose?

---
#### ¿Qué es Docker?

| VMs                                  | Docker containers                              |
| ------------------------------------ | ---------------------------------------------- |
| <img src="slides_assets/Taller de Docker\ -\ VMs.png" width=300 alt="VMs"> | <img src="slides_assets/Taller de Docker - que es docker.png" width=450 alt="Docker">   |

---
#### Terminología Docker


| Término    | Representación                                         | Equivalente en VMs |
| ---------- | ------------------------------------------------------ | ------------------ |
| Imagen     | ![[Taller de Docker - imagen - contenedores.png\|200]] | Imagen ISO         |
| Contenedor | -                                                      | Instancia VM       |
| Volumen    | ![[Taller de Docker - volumen.png\|250]]               | Disco              |

---
#### Arquitectura de Docker

![[Taller de Docker - arquitectura de docker.png]]

---
#### ¿Cómo inicio un contenedor de  Docker?

- Hello world
```bash
docker run hello-world
```

- Interactivamente:
```bash
docker run -it ubuntu bash
```

https://hub.docker.com/ (registro oficial de Docker, pero hay muchos más,...)

---
#### ¿Cómo creo una imagen de  Docker?

|                                        |                                                                 |
| -------------------------------------- | --------------------------------------------------------------- |
| ![[Taller de Docker - Dockerfile.png]] | + Receta<br>+ Cada orden es una LAYER<br>+ Cada LAYER se cachea |

```bash
docker build . -t app:latest
docker image ls | grep app
```
---
##### Conceptos extra

|                                             |                                              |
| ------------------------------------------- | -------------------------------------------- |
| Modo interactivo<br><br>(interactive + tty) | <pre>-it</pre>                               |
| Volumen                                     | <pre>-v '<HOST_PATH>:<CONTAINER_PATH>'</pre> |
| Mappeo de puertos                           | <pre>-p '<HOST_PORT>:<CONTAINER_PORT>'</pre> |
| ...                                         |                                              |

---
#### ¿Qué es Docker Compose?

![[Taller de Docker - docker compose file.png|400]]

---
## Contexto en el desarrollo de software

  - ¿Cómo containerizar una app escrita en Python para despliegue a producción? (ejemplo práctico con una app en Python)
  - ¿Cómo usar Docker DURANTE el desarrollo de software?

> [!example] Ejemplo de API + MongoDB

---
## Contexto en la administración de sistemas

- ¿Cómo usar Docker para monitorización de un sistema / app? (ejemplo práctico con Grafana + Prometheus)

> [!example] Ejemplo con Grafana + Prometheus y NTFY

---

## BONUS (si nos da tiempo)

- Overleaf dedicado corriendo como contenedor de Docker
- Alternativas a Docker
- Testcontainers
- Casos de uso real de Docker

---
#### Overleaf dedicado corriendo como contenedor de Docker

> [!example] En terminal

---

#### Alternativas a Docker

- [orbstack](https://orbstack.dev/) (exclusivo para Mac por ahora)
- [podman](https://podman.io/)
- [portainer](http://portainer.io/)

---

- Testcontainers
	- Librería para controlar Docker de manera programática desde un programa

![[Taller de Docker - testcontainers.png|700]]


---

#### Casos de uso real de docker compose

> [!example] Capturas en Obsidian

%% 

![[Taller de Docker - uso real 1.png]]

![[Taller de Docker - 2.png]]

![[Taller de Docker - 3.png]]

![[Taller de Docker - 4.png]]

![[Taller de Docker - 5.png]]

%%
