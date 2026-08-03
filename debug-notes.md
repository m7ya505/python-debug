# Debug Notes

1. reproduce: ran buggy.py, IndexError on line 4
2. hypothesis: the loop goes one index too far
3. isolate: range(len+1) reaches index 4, but the list ends at 3
4. test: printed i and saw it hit 4
5. fix: removed + 1 from range
