from pddl.logic.base import Formula, is_literal
from pddl.parser.symbols import Symbols
from pddl.helpers.cache_hash import cache_hash
import functools

@cache_hash
@functools.total_ordering
class SensingModel:
    """
    Represents a sensing model: a mapping from an observable predicate value
    to a condition (formula) under which it holds.
    """
    def __init__(self, literal: Formula, condition: Formula) -> None:
        """
        Initialize the sensing model.

        :param literal: the observable predicate or NOT predicate
        :param condition: the condition under which the literal holds
        """
        self._literal = literal
        self._condition = condition

    @property
    def literal(self) -> Formula:
        """Get the literal."""
        return self._literal

    @property
    def condition(self) -> Formula:
        """Get the condition."""
        return self._condition

    def __hash__(self) -> int:
        """Get the hash."""
        return hash((SensingModel, self.literal, self.condition))

    def __str__(self) -> str:
        """Get the string representation."""
        return f"({Symbols.MODEL_FOR.value} {self.literal} {self.condition})"

    def __repr__(self) -> str:
        """Get the string representation."""
        return f"{type(self).__name__}({repr(self.literal)}, {repr(self.condition)})"

    def __eq__(self, other):
        """Override equal operator."""
        return (
            isinstance(other, SensingModel)
            and self.literal == other.literal
            and self.condition == other.condition
        )

    def __lt__(self, other):
        """Compare with another object."""
        if isinstance(other, SensingModel):
            return (self.literal, self.condition) < (
                other.literal,
                other.condition,
            )
        return super().__lt__(other)