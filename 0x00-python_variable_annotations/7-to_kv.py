#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """"Convert str and int or float to tuple"""
    return (k, v ** 2)
