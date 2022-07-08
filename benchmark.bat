@echo off
for /l %%x in (4, 2, 24) do (
    echo ================================================================
    echo Amount of cities: %%x
    mprof run --include-children main.py --amount-of-cities %%x
)e
