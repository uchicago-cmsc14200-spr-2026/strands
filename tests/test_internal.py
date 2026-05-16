from base import BoardBase, StrandBase
from strands import StrandsGame


# Internal invariant of the StrandsGame object


def check_internal_invariant(game: StrandsGame) -> None:
    # TODO: Replace this with specific invariants regarding the
    # private instance attributes in your game logic implementation.
    # That is, add assertions about the instance attributes that
    # should be true before and after every call to the methods
    # defined in the StrandsGameBase interface.
    assert True


# Wrappers around the StrandsGameBase interface


def theme(game: StrandsGame) -> str:
    check_internal_invariant(game)
    result = game.theme()
    check_internal_invariant(game)
    return result


def board(game: StrandsGame) -> BoardBase:
    check_internal_invariant(game)
    result = game.board()
    check_internal_invariant(game)
    return result


def answers(game: StrandsGame) -> list[tuple[str, StrandBase]]:
    check_internal_invariant(game)
    result = game.answers()
    check_internal_invariant(game)
    return result


def found_strands(game: StrandsGame) -> list[StrandBase]:
    check_internal_invariant(game)
    result = game.found_strands()
    check_internal_invariant(game)
    return result


def game_over(game: StrandsGame) -> bool:
    check_internal_invariant(game)
    result = game.game_over()
    check_internal_invariant(game)
    return result


def hint_threshold(game: StrandsGame) -> int:
    check_internal_invariant(game)
    result = game.hint_threshold()
    check_internal_invariant(game)
    return result


def hint_meter(game: StrandsGame) -> int:
    check_internal_invariant(game)
    result = game.hint_meter()
    check_internal_invariant(game)
    return result


def active_hint(game: StrandsGame) -> None | tuple[int, bool]:
    check_internal_invariant(game)
    result = game.active_hint()
    check_internal_invariant(game)
    return result


def submit_strand(
    game: StrandsGame, strand: StrandBase
) -> tuple[str, bool] | str:
    check_internal_invariant(game)
    result = game.submit_strand(strand)
    check_internal_invariant(game)
    return result


def use_hint(game: StrandsGame) -> tuple[int, bool] | str:
    check_internal_invariant(game)
    result = game.use_hint()
    check_internal_invariant(game)
    return result


# Tests 8 through 11, plus invariant checking
#
# First, copy-paste these tests from tests/test_strands.py:
#   - test_play_game_G_once
#   - test_play_game_G_twice
#   - test_play_game_G_three_times
#   - test_play_game_G_more
#
# And then replace all calls to each game.method(...) with
# the corresponding wrapped version method(game, ...).

# TODO: Copy-paste and edit here
