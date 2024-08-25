import pytest
import src.main as main
import pandas
import shutil
import os

def compareCsvFiles(file1, file2):
    df1 = pandas.read_csv(file1)
    df2 = pandas.read_csv(file2)
    return df1.equals(df2)

class TestMain:
    def setup_class(cls):
        cls.parser = main.getParser()
        
        cls.inputFile = "./tests/res/example.csv"
        cls.presortedFile = "./tests/res/example_presorted_3.csv"
        
        cls.tempDir = "./tests/res-temp/"
        cls.outputFile = "./tests/res-temp/example_output_test.csv"

        shutil.rmtree(cls.tempDir)
        os.makedirs(cls.tempDir, exist_ok=True)

    def teardown_class(cls):
        pass

    def test_sort_column_error(self):
        args = self.parser.parse_args([self.inputFile, "--sort", "5"])
        with pytest.raises(IndexError):
            main.processArgs(args)
    
    def test_save_unmodified(self):
        args = self.parser.parse_args([self.inputFile, "--save", self.outputFile])
        main.processArgs(args)
        assert compareCsvFiles(self.inputFile, self.outputFile) == True
    
    def test_save_modified(self):
        args = self.parser.parse_args([self.inputFile, "--save", self.outputFile, "--sort", "-1"])
        main.processArgs(args)
        assert compareCsvFiles(self.inputFile, self.outputFile) == False
    
    def test_sort(self):
        args = self.parser.parse_args([self.inputFile, "--save", self.outputFile, "--sort", "3"])
        main.processArgs(args)
        assert compareCsvFiles(self.outputFile, self.presortedFile) == True
    
    @pytest.mark.parametrize("limit", ["-100", "0", "100", "1000", "-1", "1", "5", "-5"])
    def test_limit(self, limit):
        args = self.parser.parse_args([self.inputFile, "--save", self.outputFile, "--orig", "--result", "--limit", limit])
        main.processArgs(args)
        assert compareCsvFiles(self.inputFile, self.outputFile) == True
    
    @pytest.mark.parametrize("input", [[], ["--sort", "1"], ["./res/example.csv", "--sort"], ["--invalid-argument"]])
    def test_invalid_input(self, input):
        with pytest.raises(SystemExit):
            args = self.parser.parse_args(input)
            main.processArgs(args)
