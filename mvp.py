"""
Try to rewrite this code with Python
source: https://blog.janestreet.com/computations-that-differentiate-debug-and-document-themselves/
"""
from typing import List, Optional

"""
(** A computation involving some set of variables. It can be evaluated, and
    the partial derivative of each variable will be automatically computed. *)
type t

module Variable : sig
  (** An identifier used to name a variable. *)
  module ID : String_id.S

  (** A variable in a computation. *)
  type t

  val create : id:ID.t -> initial_value:float -> t

  (** Returns the current value of this variable. *)
  val get_value : t -> float

  (** Returns the current partial derivative of this variable. *)
  val get_derivative : t -> float

  (** Sets the current value of this variable. *)
  val set_value : t -> float -> unit
end
"""
class Variable:
  def __init__(self, id, init_val, parents:Optional[List]= None) -> None:
    self.ID = id
    self.v = init_val
    self.parents: List[Variable] = parents if parents is not None else []
  
  def __repr__(self) -> str:
    return '{}: {}'.format(self.ID, self.v)

  def get_value(self):
    return self.v

  def get_derivative(self):
    ...

  def set_value(self, v) -> None:
    self.v = v

"""
(** Constructs a computation representing a constant value. *)
val constant : float -> t
"""
def constant(id, v) -> Variable:
  return Variable(id, v)

"""
(** Constructs a computation representing a single variable. *)
val variable : Variable.t -> t
"""
def variable(id, v) -> Variable:
  return Variable(id, v)

"""
(** Constructs a computation representing the sum over some [t]s. *)
val sum : t list -> t
"""
def vsum(vars: List[Variable]) -> Variable:
  return Variable('SUM', sum([var.v for var in vars]), parents=vars)

"""
(** Constructs a computation representing the square of [t]. *)
val square : t -> t
"""
def vsquare(var) -> Variable:
  return Variable('SQUARE', var.v**2, parents=[var])

"""
(** [evaluate t] evaluates the computation [t] and returns the result, and
    updates the derivative information in the variables in [t]. *)
val evaluate : t -> float
"""
def evaluate(var):
  return ...

def expand(var, max_lvl=None, _lvl=0):
  if _lvl == max_lvl: return
  print('  ' * _lvl, var)
  for parent in var.parents:
    expand(parent, max_lvl=max_lvl, _lvl=_lvl+1)

"""
```
let computation =
  let var name initial_value =
    variable (Variable.create ~id:(Variable.ID.of_string name) ~initial_value)
  in
  let x = var "x" 2. in
  let y = var "y" 4. in
  square (sum [x; square (sum [ y; constant 1.0 ])])
;;
```
"""
def main():
  one = constant('one', 1)
  two = constant('two', 2)
  y = variable('y', 4)
  x = variable('x', 2)
  computation = vsum([y, one])
  computation = vsquare(computation)
  computation = vsum([x, computation])
  computation = vsquare(computation)
  computation = vsum([computation, two])
  # print(computation, computation.parents)
  expand(computation); print()
  expand(computation, max_lvl=2); print()
  expand(computation, max_lvl=3); print()

if __name__ == '__main__':
  main()
