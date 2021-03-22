#IS218 STATISTICS CALCULATOR

1. Team:
    * Hannah Benjamin
    * Juan Ceballos
   
2. Badges
   * [![Build Status](https://travis-ci.com/hannahbee123/is218_statcalc.svg?branch=master)](https://travis-ci.com/hannahbee123/is218_statcalc)
   * [![Coverage Status](https://coveralls.io/repos/github/hannahbee123/is218_statcalc/badge.svg?branch=master)](https://coveralls.io/github/hannahbee123/is218_statcalc?branch=master)
   
3. Task List
   * Completed by Hannah
      * Create project outline and task list
      * Formulas in statistics folder: mean, variance, std dev
      * Create calculator object
      * Input validation in helpers folder
      * Population sampling methods: simple random sampling, confidence interval, and margin of error
      * Calculator unit tests: add, subtract, multiply, divide, square, square root, mean, std dev, variance
      * Unit tests for random generator functions
      * Unit tests for statistics methods that utilize the random generator functions
   * Completed by Juan
      * Formulas in operations folder: median, mode, z-score
      * Population sampling methods: cochran's sample size, find sample size given confidence interval and width
      * Random generator class
      * Calculator unit tests: median, mode, z-score
      * Unit tests for population sampling
   
#PROJECT OUTLINE
1. Calculator object
   * Methods 
     * Add
     * Subtract
     * Multiply
     * Divide
     * Square
     * Square Root
     * Mean
     * Median
     * Mode
     * Std dev
     * Variance
     * Z-score
   
2. Operations (basic arithmetic)
   * Addition
   * Subtraction
   * Multiplication
   * Division
   * Square
   * Square root
   
3. Statistics operations
   * Mean
   * Median
   * Mode
   * Std dev
   * Variance
   * Z-score
   
4. Random generator
   * Generate random number w/o seed between range of two numbers
   * Generate random number w/ seed between range of two numbers
   * Generate list of N random numbers w/ seed and between range of two numbers
   * Select random number from list
   * Select random number from list w/ seed
   * Select N number of items from list w/o seed
   * Select N number of items from list w/ seed
   
5. Population Sampling class
   * Simple random sampling
   * Confidence interval
   * Margin of error
   * Cochran's sample size
   * Find sample size given confidence interval and width
   
6. Helper functions
   * Input validation
   
7. Tests
   * Calculator unit tests
   * Population sampling unit tests
   * Random generator unit tests
   * Statistics calculations using random generator unit tests