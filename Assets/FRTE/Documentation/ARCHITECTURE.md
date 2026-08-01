# FRTE SDK Architecture

The FRTE SDK follows a decoupled **Registry-DI** architecture. 

```mermaid
graph TD
    FRTE.Core --> FRTEContainer[FRTE DI Container]
    FRTE.Physics --> FRTE.Core
    FRTE.Materials --> FRTE.Core
    FRTE.Decoration --> FRTE.Core
    FRTE.PhotoZone --> FRTE.Core
    FRTE.Surprise --> FRTE.Core
    FRTE.Export --> FRTE.Core
```

### Decoupling Principles
- Modules register themselves to the `FRTEContainer` during the `BeforeSceneLoad` runtime execution phase using Bootstrappers.
- Inter-module communication is driven by the thread-safe `EventBus` to prevent compile-time cross-dependencies.
