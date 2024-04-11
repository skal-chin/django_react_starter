#### Extending the server through the 'core' app

The server can be extended by directly adding to the core directory. The core directory has been modularized into separate directories for models, views, and managers. Files can be added into these respective directories. Each directory has an `__init__.py` file that imports the files from that directory. This will need to be modified to include the new files.

If a new model is added, the core directory will look like this:

```bash
core/
    decorators/
    managers/
    migrations/
    models/
        __init__.py
        token_models.py
        user_models.py
        new_models.py   # ***New model file***
    utils/
    views/
```

and the `__init__.py` file in the models directory will look like this:

```python
from .user_models import *
from .token_models import *
from .new_models import *  # ***New model file***

__all__ = [
    'user_models',
    'token_models',
    'new_models'  # ***New model file***
]
```

This way, the new models will be imported if the developer imports by using the following code: `from core.models import *`. The same process can be done for views and managers.