Title: Back-to-Basics: The design philosophy of the DARPA Internet protocols
Date: 2014-06-01
Category: back-to-basics
Tags: networking, back-to-basics
Slug: b2b-darpa-design-policy-clark
Author: S.S.

<!-- PELICAN_BEGIN_SUMMARY -->
I've always been intrigued by the technologies that have had their start as research projects funded by [DARPA](http://en.wikipedia.org/wiki/DARPA). The Internet, in my opinion, is one project that has touched more lives than any other DARPA initiative. I first read this paper as part of my [graduate course](http://www.ecs.umass.edu/ece/wolf/courses/ECE671/) in computer networking, and it feels good to start right from the paper that got me interested in the area of networked systems. This paper is by [David Clark](http://en.wikipedia.org/wiki/David_D._Clark) and is one of the seminal papers in computer networking. It discussed about some of the core principles/motivations behind the design of the Internet protocols/architecture.
<!-- PELICAN_END_SUMMARY -->


The primary goal of the DARPA Internet initiative was to connect existing heterogeneous administratively separate networks together to form a larger network for the purposes of resource sharing, ease administration, etcetera. The underlying multiplexing mechanism for network resource sharing used was packet-switching since that was proven to be more robust and resilient to failures in ARPANET. Moreover, store-and-forward packet forwarding mechansim implemented in packet processors was chosen for similar reasons.

<img src="images/articles/clark-darpa-packet-switched-network.jpg" alt="clark" style="width: 12cm;"/>

The fundamental goal was further sub-divided into a prioritised list of requirements. In order of priority,

1. Internet communication must continue despite loss of networks or gateways
2. The Internet must support multiple types of communications service.
3. The Internet architecture must accommodate a variety of networks.
4. The Internet architecture must permit distributed management of its resources.
5. The Internet architecture must be cost effective.
6. The Internet architecture must permit host attachment with a low level of effort.
7. The resources used in the internet architecture must be accountable.

The military applications of the network meant that the items at the top of the list received more attention - one would want a communications network able to tolerate hostile enemy fire and able to sustain loss to parts of the network versus a network where resources accountability or cost effectiveness was of major importance. 

The seven items in the list can be categorized into three broad areas:

* Reliability (1)
* Flexibility (2, 3, 4, 6)
* Cost Efficiency and Accountability (5, 7)

Reliability was achieved by a combination of packet-switched networking, and a design that resulted in a layered network protocol stack. In 1964, [Paul Baran](http://en.wikipedia.org/wiki/Paul_Baran) had proved the reliability of packet-switched networking when subject to network failures in his published paper, "[On Distributed Communications Networks](http://www.rand.org/content/dam/rand/pubs/research_memoranda/2006/RM3420.pdf)." Layering of protocols meant that the lower layers stored as little information about the state of packet connections as possible, and instead, relegated that responsibility to upper layers which terminated in application on the end-hosts. This resulted in an architecture where the network was comprised of simple, stateless devices devoid of responsibility of ensuring reliable packet delivery, and instead pushed the responsibility of state management, retransmissions on failures etc. to upper-layer protocols and applications on the end-hosts. Clark called this *fate-sharing*. Moreover, this layered approach with the a datagram being the fundamental building block meant that the network could support multiple types of transport services with application specific requirements.

The result is a global scalable decentralized network capable of connecting millions of systems and transporting data. Today, it is impossible to imagine communication, business, education and entertainment without the Internet, and is widely treated to be just another utility service.

------------
####References:

__The Design Philosophy of the DARPA Internet Protocols__ D. Clark. In Symposium proceedings on Communications architectures and protocols (SIGCOMM '88), ACM, New York, NY, USA, 1988.

__On Distributed Communications Networks__ P. Baran, Communications Systems, IEEE Transactions on In Communications Systems, IEEE transactions on, Vol. 12, No. 1. pp. 1-9, March 1964.
