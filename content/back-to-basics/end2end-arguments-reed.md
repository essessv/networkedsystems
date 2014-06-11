Title: Back-to-Basics: End-to-End Arguments in System Design
Date: 2014-06-05
Category: back-to-basics
Tags: networking, back-to-basics
Slug: b2b-end2end-arguments-reed
Author: S.S.

<!-- PELICAN_BEGIN_SUMMARY -->
The paper by Saltzer, Reed and Clark talks about the importance of moving functionality away from the lower layers of a networked system and placing them higher up the stack and closer to the applications, i.e., on the end-systems. The paper argues, with examples, that
<!-- PELICAN_END_SUMMARY -->
the end-to-end principle is the best approach for the design of networked systems. Two issues seen in systems where the lower layers implement some of the functionality are:

1. The variety of possible application requirements means there will be some applications whose requirements aren't satisfied by the communication system. Such systems will choose to implement the functionality higher up the stack anyway. Some of the functionality might be duplicated.

2. Introducing functionality into the lower layers of the stack introduces a kind of rigidity into the system. Applications that may not require the additional functionality cannot choose to opt out and that may result in certain performance implications for the application.

The authors use various examples to support their argument of moving the functionality away from the network and onto the end-systems:

* _Reliable File Transfer_ - there could be a host of problems that may occur when transferring a file from a host A to host B - from disk errors, to network transmission errors to glitches in the gateways themselves. Implementing reliability features such as retry mechanisms, error checks, sequencing, etc., in the lower layers of the network stack will only reduce the probability of the network being the problem. However, the end-systems still have to implement application-specific (file transfer, in this example) reliability mechanisms. Another caveat is the performance impact of having these reliability mechanisms in the network itself.
* _Delivery Guarantees_ - it does not make sense for a communications network to acknowledge delivery of data to a destination host. This can be a very application specific acknowledgement, for example, for cases where a message results in an acknowledgement only once the message has been processed by the target application. Such cases are out of purview of the communications network.  
* _Secure transmission_ of data - the application should implement an end-to-end encryption, and perform key management. Relegating this responsibility to the network makes the data vulnerable en route to the target application.
* _Duplicate message transmission_
* _Guaranteeing FIFO message delivery_
* _Transaction management_

The end-to-end system design of the Internet is the reason why it has been successful today. Operating systems on the end-hosts implement abstractions which developers can use to interface with the network stack, with functionality like reliability, etc., implemented in the upper layers (TCP). The design reduces the amount of functionality implemented at the lower layers - IP provides a best-effort service and is deemed to be an unreliable protocol (packet corruptions, loss, out-of-order and duplicate packets) with minimal amount of error checking by way of checksums. 

In conclusion, the end-to-end argument is a guideline to follow when designing networked systems. As stated in the paper, 
>..the end-to-end argument is not an absolute rule, but rather a guideline that helps in application and protocol design analysis; one must use some care to identify the end points to which the argument should be applied. Using the end-to-end argument sometimes requires subtlety of analyis of application requirements.

------------
####References:
__End-to-end arguments in system design__ J. H. Saltzer, D. P. Reed, and D. D. Clark. In ACM Transactions on Computer Systems, 1984. 


