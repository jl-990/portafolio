# Análisis y mejora de estructura de carpetas

## Diagnóstico rápido de la propuesta original

Fortalezas:
- Tiene separación base por capas (`core`, `data`, `modules`, `api`, `frontend`, `analytics`, `docs`, `scripts`).
- Incluye documentación y scripts operativos desde el inicio.
- Orden numérico útil para onboarding.

Riesgos detectados:
1. `02_modules` mezcla dominio y aplicación (puede crecer con acoplamiento).
2. `03_api` y `04_frontend` están vacíos sin una convención interna.
3. Falta una capa explícita de **application/use-cases** para orquestar reglas.
4. No hay carpeta de **tests** transversal.
5. No hay separación de entornos (`dev/staging/prod`) ni prácticas de seguridad.
6. `07_scripts` mezcla automatización de negocio y plataforma.
7. Falta un espacio claro para observabilidad y CI/CD.

## Objetivos de la versión mejorada

- Reducir acoplamiento entre dominio, interfaces y datos.
- Escalar sin perder trazabilidad técnica/funcional.
- Facilitar testing, despliegue y operación.
- Mantener tu convención numérica para navegación rápida.

## Estructura sugerida (v2)

La estructura propuesta está en `docs/estructura_sugerida_v2.json`.

Principales cambios:
- `00_core` evoluciona a `00_governance` (config, seguridad, contratos).
- `02_modules` se convierte en `02_domain` (modelos/servicios/repos/tests por bounded context).
- Se agrega `03_application` para casos de uso y orquestación.
- `03_api` + `04_frontend` pasan a `04_interfaces` (REST/UI/CLI como puertos).
- `07_scripts` escala a `07_platform` (scripts + infra + CI/CD + observabilidad).
- Se agrega `08_tests` para estrategia de pruebas integral.

## Reglas recomendadas de arquitectura

1. **Dependencias unidireccionales**
   - `interfaces -> application -> domain`
   - `data/platform` no deben contener lógica de negocio.

2. **Contratos primero**
   - Definir esquemas en `00_governance/schemas`.
   - Versionar OpenAPI y contratos de eventos.

3. **Módulos de dominio autocontenidos**
   - Cada contexto (`turnos`, `combustible`, `agenda`) con `models`, `services`, `repositories`, `tests`.

4. **Observabilidad mínima obligatoria**
   - Logs estructurados por capa + métricas de latencia/errores.

5. **Testing por pirámide**
   - Unitarias en dominio.
   - Integración en aplicación/datos.
   - Contrato para API.
   - E2E para flujos críticos de frontend + backend.

## Plan de adopción por fases

### Fase 1 (rápida)
- Crear `08_tests` y convenciones de naming.
- Definir estructura interna de `api` y `frontend`.
- Separar scripts de negocio vs scripts de plataforma.

### Fase 2 (estabilidad)
- Extraer casos de uso a `03_application`.
- Mover reglas de negocio de controladores a dominio/aplicación.
- Establecer contratos OpenAPI + validaciones compartidas.

### Fase 3 (escala)
- Incorporar CI/CD y observabilidad completa.
- Agregar data quality y marts analíticos.
- Formalizar ADRs en `06_docs/decisions`.

## Convención de nombres sugerida

- Carpetas: `snake_case`.
- Módulos: por capacidad de negocio (`turnos`, `combustible`, `agenda`).
- Versionado de API: `v1`, `v2` dentro de `interfaces/api/rest`.
- Scripts ejecutables: prefijo por dominio (`data_`, `infra_`, `ops_`).
