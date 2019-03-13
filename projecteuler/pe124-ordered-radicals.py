#!/usr/bin/env python
# coding=utf-8

"""124. Ordered radicals
https://projecteuler.net/problem=124

The radical of _n_ , rad( _n_ ), is the product of the distinct prime factors
of _n_. For example, 504 = 2 3 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad( _n_ ) for _1_ ≤ _n_ ≤ 10, then sort them on rad( _n_ ),
and sorting on _n_ if the radical values are equal, we get:

**Unsorted**

|  |

**Sorted**  
  
---|---|---  
  
![](images/spacer.gif)**_n_**

|

![](images/spacer.gif)**rad( _n_ )**

| ![](images/spacer.gif)  
|

![](images/spacer.gif)**_n_**

|

![](images/spacer.gif)**rad( _n_ )**

|

![](images/spacer.gif)**k**  
  
1

|

1

|  |

1

|

1

|

1  
  
2

|

2

|  |

2

|

2

|

2  
  
3

|

3

|  |

4

|

2

|

3  
  
4

|

2

|  |

8

|

2

|

4  
  
5

|

5

|  |

3

|

3

|

5  
  
6

|

6

|  |

9

|

3

|

6  
  
7

|

7

|  |

5

|

5

|

7  
  
8

|

2

|  |

6

|

6

|

8  
  
9

|

3

|  |

7

|

7

|

9  
  
10

|

10

|  |

10

|

10

|

10  
  
Let E( _k_ ) be the _k_ th element in the sorted _n_ column; for example, E(4)
= 8 and E(6) = 9.

If rad( _n_ ) is sorted for 1 ≤ _n_ ≤ 100000, find E(10000).
"""
