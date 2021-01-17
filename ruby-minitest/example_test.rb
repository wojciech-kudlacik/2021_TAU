require 'minitest/autorun'
require_relative "example"

class ExampleTest < Minitest::Test
    
    def setup
        @example = Example.new
    end

    def test_ask_returns_string
        assert @example.hello_world == "hello world"
    end

    def test_ask_returns_number
        result = @example.add_numbers(2, 2)
        assert_equal 4, result
    end

end