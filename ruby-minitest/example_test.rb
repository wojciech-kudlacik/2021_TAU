require 'minitest/autorun'
require_relative "example"

class ExampleTest < Minitest::Test
    def test_ask_returns_string
        example = Example.new
        assert example.hello_world == "hello world"
    end

end