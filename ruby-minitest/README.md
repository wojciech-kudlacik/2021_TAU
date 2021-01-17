# Assignment 5 - Testing Framework
The goal of this assignment was to choose and present one testing framework and also add some example code.

## About
Minitest comes prepackaged with every standard Ruby distribution. Minitest is often comparaed to Rspec, which has arguably more features, but for most cases Minitest will do just fine. 

Minitest provides a complete testing suite for your needs - supporting TDD, BDD, mocking, and benchmarking.

### Packages
minitest/test is a small and incredibly fast unit testing framework. It provides a rich set of assertions to make your tests clean and readable.

minitest/spec is a functionally complete spec engine. It hooks onto minitest/test and seamlessly bridges test assertions over to spec expectations.

minitest/benchmark is an awesome way to assert the performance of your algorithms in a repeatable manner.

minitest/mock by Steven Baker, is a beautifully tiny mock (and stub) object framework.

minitest/pride shows pride in testing and adds coloring to your test output.

minitest/test is meant to have a clean implementation for language implementors that need a minimal set of methods to bootstrap a working test suite. For example, there is no magic involved for test-case discovery.

## Setup
You need to have Ruby installed. Preferably anything above 2.2.
Refer to [this guide](https://www.ruby-lang.org/en/downloads/) on the official Ruby website on how to install it on different OS.
[RVM](https://rvm.io/) might come in handy as well.

But, if you won't be able to run it, consider creating a Gemfile (or you might already have it present in your project) and add this to it:

```ruby
#Gemfile
source 'https://rubygems.org'

gem 'minitest'
```

and then run:
```bash
bundle install
```

## How to run
In order to run the example tests present in repo all you need to do is
```bash
cd into/project/path/ruby-minitest/
ruby example_test.rb
```
Example output
![Imgur](https://i.imgur.com/a7xClmH.png)

## How to use Minitest
Setting up Minitest test suite is a relatively easy task.

Typically, test suites are stored in a **tests** directory, but its not required. It's good practice, tho.

There are no standardized conventios when it comes to naming your test suites. It's often suggested to establish your own naming conventions inside the project and stick to them. For example: staring each test file with **test_**.

All test files will require some boilerplate code:

![Imgur](https://i.imgur.com/c4CIdYf.png)

The test files will start will requiring **minitest/autorun** - this package includes everything you need to run most basic tests, and it ensures that all of the tests in your test suite will be run automatically when you run the test suite.

The next step is to require the files that contain the code that you want to test. You will most likely use **require_relative** to get them.

The test class will inherit methods from Minitest::Test that's why you do **ExampleTest < Minitest::Test**.

And then you can write your tests - remember that each method that you want to be a test, has to start with **test_**. 

If you have used an assertion based testing framework before, you should be fine.

Helpful list of Minitest functionalities can be found [here](https://devdocs.io/minitest/).

## Useful Links

[Ruby](https://www.ruby-lang.org/en/)

[RVM](https://rvm.io/)

[Minitest Docs](https://devdocs.io/minitest/)

[Minitest Github](https://github.com/seattlerb/minitest)
