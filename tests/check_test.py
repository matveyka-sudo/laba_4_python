from src.proc import check
from src.generator_1 import Source
from src.generator_2 import Source1
from src.generator_3 import Source2




class Test:
    def test_s(self):
        assert check(['123']) == []
        assert check([Source])==[]
        assert check([Source1]) == []
        assert check([Source2]) == []