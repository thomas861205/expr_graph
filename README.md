# expr_graph
Inspired by [this post](https://blog.janestreet.com/computations-that-differentiate-debug-and-document-themselves/)
tldr; an expression is constructed as a graph (DAG to be specific). Good side effects are expanding the expression on a different level and can easily support calculation of derivative.
```
>>> python mvp.py
 INNERPRODUCT: 26375000.0
   SUM: 26375000.0
     PRODUCT: 7720000.0
       april aum: 10000000
       april weight: 0.772
     PRODUCT: 9180000.0
       may aum: 12000000
       may weight: 0.765
     PRODUCT: 9475000.0
       june aum: 12500000
       june weight: 0.758

 INNERPRODUCT: 26375000.0
   SUM: 26375000.0

 INNERPRODUCT: 26375000.0
   SUM: 26375000.0
     PRODUCT: 7720000.0
     PRODUCT: 9180000.0
     PRODUCT: 9475000.0
```
