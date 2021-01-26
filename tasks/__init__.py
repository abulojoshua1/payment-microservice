
from invoke import Collection

from tasks import invoke_utils

ns = Collection()

ns.add_task(invoke_utils.run_dev)
ns.add_task(invoke_utils.run_prod)
ns.add_task(invoke_utils.lint_py)
ns.add_task(invoke_utils.test_py)
ns.add_task(invoke_utils.isort)
