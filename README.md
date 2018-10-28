# Band service skeleton template

## How to use it

#### Install Cookiecutter

```bash
pip install -U cookiecutter
```

#### Use template

Go to your images directory

```bash
cd my_images
```

Run generator

```bash
cookiecutter git+https://github.com/rockstat/band-skeleton-py
```

Answer for questions. After you can find service files at directory with project name.

Example
```bash
~/project ❯❯❯ pip install -U cookiecutter

Collecting cookiecutter
    100% |████████████████████████████████|

~/project ❯❯❯ cd my_images

~/p/my_images ❯❯❯ cookiecutter git+https://github.com/rockstat/band-skeleton-py

project_slug [some_service]: new_service
project_title [Some service]: New service
project_short_description [Band platform microservice for]:
version [0.1.1]:

~/p/my_images ❯❯❯ cd new_service

~/p/m/new_service ❯❯❯ make start-dev

2018-10-26 15:34.48 [info     ] final configuration            [band] settings={'name': 'new_service', 'env': 'development', 'listen': '0.0.0.0:8080', 'redis_dsn': 'redis://redis:6379', 'ch_dsn': 'http://default:default@host:9090/stats', '_pid': 528, '_cwd': '/home/theia/project/my_images/new_service'}
2018-10-26 15:34.49 [info     ] Attaching scheduler            [band.bootstrap]
2018-10-26 15:34.49 [info     ] Attaching redis RPC            [band.bootstrap]
2018-10-26 15:34.49 [info     ] Registered worker promote      [band.registry]
...
```

## License

```
Copyright 2018 Dmitry Rodin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```