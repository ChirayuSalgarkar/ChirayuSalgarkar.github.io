---
title: "Modern C++ Day 1"
excerpt: "A man realizes he's incompetent"
---
_NOT FINISHED_

Now that I'm in my internship, which uses a lot of modern C++, I realize that I know nothing about modern C++, in the real version of the world. I've also found that every time I ask questions, the smartest thing to do according to my employee friends is to ask GenAI, usually Claude. In their defence, Claude is extraordinarily good at this, but I want to be good enough at C++ that I can recognize why Claude is good at writing code (i.e. I can understand the code it's writing). I feel like writing a blog is a good start. 


## So why even use modern C++?

Some of my undergrad friends were big fans of FORTRAN. This is partially because our CS program had a professor that was a known FORTRAN evangelist, but I thought that was silly CS major energy. I wasn't a computers guy, I was a biomedical engineer. So, I used MATLAB, reluctantly using Python my senior year because I could write dirty code for classes I didn't care about in Python using Colab. (In retrospect, I probably should have learned FORTRAN, but the other languages did what I needed at the time.) But, the first purely CS class I ever took, Data Structures and Algorithms, was a C++ class. I liked the class, so I gained a soft-ish spot for C++, and I got excited when this internship said they were mainly C++ devs. But when I looked at the code, I got lost a lot. 

Why was this? Partially, it was rust on my end. But the real reason was that _modern_ C++ is almost a different language because now people think about the toolbox differently. This is particularly true in the work I'm doing right now, which involves a lot of parallel programming. So now, I care about things like Multi-threading, and words like CMake and clang (how do you even pronounce clang? Is it C-Lang or the sound you make when you drop pans?) actually mean something. But this is mainly to try to document the fruitless path I'm going through.

In general, I'm going to use Changkun Ou's work as well as the C++ High Performance, Second Edition to try to help me here. This will also force me to cite things correctly. 

I think the first thing I'm going to talk about, though is stacks and heaps. Why? They matter way more than you think for memory allocation, which is the entire ballgame here. 
Consider the following code segment:
```cpp

class Car 
{
    public:
        Car(int doors)
            : doors_(doors) {}
    
    private:
        int doors_{};
};

auto foo()
{
    auto num_doors = 2;
    auto car1 = Car(num_doors);
    auto car2 = Car(num_doors);
    // ...
}
```

{% include godbolt.html link="https://godbolt.org/e" %}

Here, everything is being placed in the stack. so the order of the stack is num_doors (int), car1: Car (object), and car2: Car (object). This is interesting. Compare this to Java, where num_doors (int) and two references to car1 and car2 are on the stack, and the Car objects will be on the heap. Why does this matter for parallel programming? For one, heaps are not great at fast memory allocation and deallocation. Stacks are way faster than the heap. But this also means that C++ engineers can easily shoot themselves in the foot. 

More importantly, each thread has its own stack. This means stack allocation is thread-local, while the heap is shard along to all threads. I hopefully will get more into that later at some point. 
