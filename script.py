from core.bot import Robot, spawn_robots
from core.geo import Direction
from core.models import Route
from core.route import RouteBuilder


# We can either use provided API

route = RouteBuilder(name='Example route')\
    .start(245, 161)\
    .step(5, Direction.NORTH)\
    .right()\
    .reach('Statue of Old Man with Large Hat')\
    .step(25, Direction.WEST)\
    .left()\
    .step(3)\
    .build()

# Or read many routes from yaml
# ```
# - name: 'My route'
#   start: '10:10'
#   steps:
#     - north: 3
#     - east: 3
#     - right:
#     - right:
#     - right:
#     - forward: 3
#     - reach: 'Saint Valley'
#
# - name: 'Route only for packagers'
#   target: "Packagers"
#   steps:
#     - north: 3
#     - east: 3
#     - right:
#     - forward: 10
#
# ```

# Create routes from file and save all to database
routeset = RouteBuilder.from_yaml('route.yml').save()  # class RouteSet - wrapper

# Robot has own API. Also robots can be separated to groups for further relevant route consuming
r = Robot().forward(3).forward(5)

# Also robot can interpret route which can be created by many different ways
for i, route in enumerate(Route.objects.all(), start=1):
    print(f'Route: {i}')
    r.load(route)

print(f'Arrived: {r.position}')

# Route can be targeted to some dedicated robot group.
spawn_robots(3, group='Packagers')

# we can notify all our robots about all our routes (groups also considered), to execute instructions.
routeset.notify_bots()

# notify only 'New group' about this route
route.notify(target='New group')

