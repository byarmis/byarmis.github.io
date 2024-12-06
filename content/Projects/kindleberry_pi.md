Title: Kindleberry Pi Zero W
Date: 2018-01-03
Tags: eink, raspberry pi
Summary: Impractical portable computing

## What

This is what I'm calling the Kindleberry Pi Zero W.

![Kindleberry Pi Zero W |]({filename}/images/KindleberryPi/KindleberryPiZeroW.jpg)

Yeah, I know it's a mouthful, it just seemed like the only appropriate name.
It's a Raspberry Pi Zero W, a Kindle Touch, and a Bluetooth keyboard, all routed through my phone acting as a router and wireless access point.
It's a portable, minimalistic-ish computing solution in search of a problem.
And I really like it!

## Why

I remember reading about a [Kindleberry Pi](https://maxogden.com/kindleberry-wireless.html) that consisted of a newer Kindle and an older Raspberry Pi.
This is an update to that update.
I figured, since I have a Kindle sitting around doing nothing, a spare-at-the-moment Raspberry Pi Zero W, and a nice lazy long weekend ahead of me, I might as well see how far I can get with setting it up.
Turns out, pretty far!

At the end of the weekend (plus an evening to iron the kinks out), I have something that I can throw in a bag and take on a plane for fun, portable computing.
Ok, there might also be a slight hipster air about the whole thing that also calls to me, sue me.

## How

### Hardware

* Kindle

    ![Kindle >*]({filename}/images/KindleberryPi/Kindle.jpg)

    I'd heavily suggest using one that you already have and not buy it for this project exclusively.
    While fun, I wouldn't say it's worth the price of entry.
    
    I have a Kindle Touch that I've had since college and it's still kicking.  
    Not sure the exact version, but the serial number starts with `B00F`, if that helps at all.
    This is the 3G version, but that doesn't matter for this.

    That may be an interesting addition though-- using the cellular connection to SSH to the Pi instead of WiFi.  I would worry about the "free" cellular internet being turned off though.

    * Used Kindle Touches start at around $[30 on Amazon](https://www.amazon.com/gp/offer-listing/B005890G8Y/ref=olp_twister_child?ie=UTF8&mv_configuration=0) and new ones can go up to $[250](https://www.amazon.com/All-New-Amazon-Kindle-Oasis-8GB-Grey/dp/B06XD5YCKX/ref=sr_1_5?ie=UTF8&qid=1515474420&sr=8-5&keywords=kindle), but be sure to make sure that whichever one you end up getting is jailbreak-able 

* Raspberry Pi Zero W / Case / microSD Card

    ![RaspberryPi >*]({filename}/images/KindleberryPi/PiZero.jpg)

    It doesn't have to be the Zero, but I do suggest having one with built-in WiFi / Bluetooth-- it's one less thing that you have to worry about setting up.
    Plus, I like not having dongles sticking out of the Pi.
    I heavily suggest also getting a case for the Pi since you'll probably end up throwing it in a bag.
    The microSD card is a given-- at the moment, I'm using a 16GB card I had laying around and have a cheap 32GB on the way.
    Even still, I'm sitting at less than 10% used and I can't imagine using significantly more.

    * Prices start at $[10](https://www.adafruit.com/product/3400), depending on [bundles](https://www.amazon.com/gp/product/B06XD18H6K/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1).
    Note that I don't suggest the bundle linked, unless you, like me, are driven to order things from Amazon for other reasons (gift cards, etc.).

    * Cases cost around the same, starting at around $[6](https://www.amazon.com/Zebra-Zero-Raspberry-Wireless-Heatsinks/dp/B071RRYCQ4/ref=sr_1_5?ie=UTF8&qid=1515474323&sr=8-5&keywords=raspberry+pi+zero+case), depending on [bundles](https://www.amazon.com/gp/product/B06XD18H6K/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1)

    * MicroSD cards can be pretty cheap, starting at around $[8 and going up](https://www.amazon.com/SanDisk-Ultra-Micro-Adapter-SDSQUNC-016G-GN6MA/dp/B010Q57SEE/ref=sr_1_6?s=electronics&ie=UTF8&qid=1515474282&sr=1-6&keywords=micro+sd), depending on speeds and capacity.

* Battery Bank

    ![Battery >*]({filename}/images/KindleberryPi/Battery.jpg)

    In order for this to be portable, you need a battery bank powering the Pi.
    I'm using [this](https://www.amazon.com/dp/B00Z9QVE4Q) one from Anker and I'm liking it so far.

    I was originally going to use a battery pack with roughly twice the capacity, but that one's just too big and the Pi Zero just isn't that power hungry.

    * Battery banks cost $[10 and up](https://www.amazon.com/Aibocn-External-Battery-Charger-Flashlight/dp/B013HIR1Q2/ref=sr_1_5?ie=UTF8&qid=1515474772&sr=8-5&keywords=battery+bank).
    The [Anker I used is $30](https://www.amazon.com/gp/product/B00Z9QVE4Q/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1)

* Keyboard

    ![HHKB >*]({filename}/images/KindleberryPi/HHKB.jpg)

    I'm using an HHKB modified with a Bluetooth controller.
    The keyboard was purchased from [EliteKeyboards](http://elitekeyboards.com/products.php?sub=pfu_keyboards,hhkbpro2&pid=pdkb400b), but you can also probably get it from Amazon; the controller was purchased from [1UPKeyboards](https://1upkeyboards.com/hhkb-bluetooth-controller.html) with a battery from either Adafruit or Sparkfun.
    I'm a fan of mechanical keyboards and this one is my favorite-- it's ok to say that since that's what I'm using to write this.
    I love its portability, layout, and switches.

    When I travel, I like to take one of my keyboards with me and it's usually the HHKB, so it makes sense that I'd use this one with my portable-setup-to-be.
    I know this isn't a keyboard for everyone and you can most definitely use whatever keyboard you'd like-- Bluetooth being another battery you have to charge but one less wire to worry about.
    It can be a little annoying setting up a Bluetooth keyboard if you aren't already connected, so heads up there.

    * This specific keyboard cost around $220, the controller board cost $85, and the battery probably cost around $10 or so.

* Router

    ![PortableHotspot >*]({filename}/images/KindleberryPi/PortableHotspot.jpg)

    I talk more about this below, but you need something to act as a router for traffic between the Pi and the Kindle.
    It's even better if it has an internet connection for minimal web connectivity.
    I've used mine for pretty much just updates and git activity.
    [I use my Pixel 2 as the router](https://support.google.com/nexus/answer/2812516?hl=en), but I also used a portable cellular hotspot briefly and it worked.

    * A cursory search indicates portable routers cost $40 and up on Amazon, but your wireless carrier may have deals.
    I use my Pixel 2, so that's "free"

* Adapters and cables

    ![Cables >*]({filename}/images/KindleberryPi/Cables.jpg)

    By my count, there's four different batteries and three different connectors involved with all of the electronics in play here:

    * Keyboard (mini USB)
    * Battery pack (micro USB)
    * Kindle (micro USB)
    * Phone (USB-C)

    The battery bank I got comes with a little bag and in it, I also have two stubby micro USB cables, a USB micro-to-C adapter, a USB micro-to-mini adapter, and a USB-OTG adapter.
    Fortunately, all the cables, adapters, and the Pi Zero all fit in the bag with the battery so it's all still surprisingly portable.

    * You can get a multipack of [USB-OTG adapters for $4.50](https://www.amazon.com/CHENYANG-Ultra-Adapter-Connector-Tablet/dp/B015GZOHKW/ref=sr_1_14?ie=UTF8&qid=1515474151&sr=8-14&keywords=usb+otg) and a really short [micro-USB cable for around the same price](https://www.amazon.com/gp/product/B013G4EAEI/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1).

So, the cost can range from a few bucks to a few hundred, depending on what you already have and what you end up ordering.

### Jailbreak the Kindle

This part of the process is almost definitely the one that I'm least-familiar with.
After a bit of Googling and browsing some forums, there's a whole community that I had no idea existed. 
Deciphering some of the quite old posts can be a little difficult, but there's probably a guide out there on how to upgrade / downgrade your Kindle to a jailbreak-able firmware version and then jailbreak it.
For my Kindle Touch, I didn't have to change the firmware version even though I thought I did.
That made trying to jailbreak a little interesting-- I couldn't figure out why downgrading the firmware wasn't working when I was really accidentally trying to upgrade to an incompatible version.
I finally found and used [this](https://www.mobileread.com/forums/showthread.php?t=186645) guide but you will probably have to Google around for your specific Kindle and firmware version.

Next, you have to install [KTerm](https://www.fabiszewski.net/kindle-terminal/) and [USB Networking](https://www.mobileread.com/forums/showthread.php?t=186645).
The former installs a terminal and the latter installs both an SSH client and server.
I modified my KTerm configuration file to automatically start in landscape mode and a slightly smaller font size, but that's all easy to change once running by tapping with two fingers. 

### Set up the Raspberry Pi

Download the current version of Raspbian (Lite-- we don't need any GUI components) and flash it to the microSD card.
Set up the appropriate WiFi connectivity information in `/etc/wpa_supplicant/wpa_supplicant.conf` or by modifying a `wpa_supplicant.conf` file in the `/boot/` directory.
I also suggest putting an empty file called `ssh` in the `/boot/` folder to enable SSH for the Pi.

Boot up, set up, update, and modify however you prefer.
I do suggest enabling automatically logging in to the terminal via `sudo raspi-config`.
Among other things, be sure ton install GNU Screen (`sudo apt-get install screen`).
My `.screenrc` file is pretty boring-- I remapped `<C-a>` to ``<C-`>`` since I like using the former in Vim to increase the next number on the current line.

I modified my `.bash_profile` to be the following:

```
stty rows 29
stty columns 72

if [ -z "$STY" ];  then
	exec screen -xAR
fi
```

Depending on how you have your font size set up, you may have to play around with the number of rows and columns.
You can modify those via the terminal without having to re-connect or restart the Pi.

#### The problem of the dashed lines

For quite a while, I was getting these weird dashed lines a couple rows up from the bottom of the terminal on the Kindle once I connect to the Pi.
No amount of playing around with the number of rows and columns (via `stty` commands) in either the Pi or the Kindle helped things.

The solution ended up being setting the resolution in the Pi's `/boot/config.txt` to be that of the Kindle (mine's 800 x 600).
If you run into a similar problem, update the corresponding lines in the file to be the following:

```
framebuffer_width=800
framebuffer_height=600
```

Reboot (`sudo reboot`) and you should be good to go.

### Set up the networking components

I originally started this project trying to get the Pi to act as a wireless access point and have the Kindle connect to that.
I found a couple guides online for how to set a Raspberry Pi up as a portable router, using the ethernet jack as an internet connection.
Even though I could use a USB-to-ethernet adapter with the Pi Zero, that kinda defeated the purpose of a portable computing setup.
I was able to create a network that I could view and connect to, just none of the devices I tried would stay connected since I don't think they were ever successfully assigned an IP address.
I now couldn't SSH into the Pi anymore since it's no longer connected to any network.

It was around this time that I realized disabling the hardware serial pins was probably a bad idea-- I now couldn't connect to or communicate with the Pi at all, from what I could tell.
Having a little [3.3v USB-to-serial adapter](https://www.sparkfun.com/products/9873) was helpful here though.
Make sure that you don't connect power if it's not a 3.3v adapter-- even if it is, I still wouldn't suggest it since the current requirements might be more than the regulator on the FTDI chip can provide.

I reflashed the SD card and had a good think in the shower.
It dawned on me that I would probably want the option for an internet connection at some point so I shouldn't really use the Pi as a router at all.

I had a portable cellular hotspot in a bag and connected everything to that.
Still no internet connection since I hadn't topped up the SIM card, but everything was working.

Another forehead-smacking moment later, I set my phone up as a hotspot and now everything's grand.
There's one less thing that I need to carry around and keep charged, I don't have to worry about paying extra for internet access, and I have access to the Pi via a terminal that's not on the Kindle should I want to use that (I installed [Terminus](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client), but there's a bunch of good ones out there).

### Setting up SSH keys on the Kindle (Optional)

I suggest setting up SSH keys on the Kindle and on the Pi so that you don't have to type the password into the Kindle-- the small keyboard and delay is really not conducive to accurately typing in passwords.
I also suggest generating the keys on the Pi and not the Kindle since it pegged my Kindle's processor to 100% for north of five minutes when I tried and ended up having to kill the process.

* Generate the public / private key pair

    ```
    $ ssh-keygen -t rsa -b 4096
    ```

* Enter a passphrase if you want-- I didn't
* I suggest naming the file to something a little more descriptive than just `id_rsa`.
* Copy the private key from the `~/.ssh/` folder in the Pi to the Kindle using something like SFTP or SCP
* Add the public key to the list of authorized keys on the Pi by running `cat <PATH TO PUBLIC KEY> >> ~/.ssh/authorized_keys`
* Start the SSH agent on the Kindle by running `eval $(ssh-agent -s)`
* Add the private key: `ssh-add <PATH TO SSH FILE>`

Should be good to go!
I put the last two steps plus the SSH command itself in a simple shell script on the Kindle and run that to connect to the Pi since the `ssh-agent` frequently needs to be started (and starting it again has no ill effects).

## Current State

Texas.

----

![Current State |*]({filename}/images/KindleberryPi/KindleberryPiZeroW_with_cables.jpg)

I mostly just use this around the house at the moment and bring it to the office once or twice to show off to coworkers.
I mostly plan on using it for writing blog posts and playing around with Python.
I'll be travelling with this in February, so we'll see how it holds up on an actual plane (and around *normal* people).

## Next Steps

First and foremost, I need to design and print a stand for the Kindle.
As it stands now, it doesn't.
It's propped up against my monitor, a random wall, or anything that I can find depending on where I'm using it.
The font size, in order to fit any respectable amount of text on the screen, is ever so slightly too small given the current size of my desk or where I've tried setting this thing up.
I imagine on a plane it'd be not as bad since you can prop it against the chair in front of you, but you might have to struggle with it sliding around.

I should probably set up OpenVPN on the Pi since I went through the trouble of setting up a Raspberry Pi3 at home running [PiVPN](http://www.pivpn.io/) and [PiHole](https://pi-hole.net/).
I also like the idea of having two Pis that I set up communicate with each other.

I'm still not convinced of the battery setup.
I do like having the option for multiple outputs but I don't like not having passthrough charging.
In order to charge the battery, it can't be powering anything, preventing it from acting as a UPS for the Raspberry Pi Zero or anything like that.
In order to charge the battery, the Pi has to be shutdown.
The [PowerBoost 1000](https://www.adafruit.com/product/2465) from Adafruit connects to a naked LiPo battery and allows for charging passthough.
There are holes and mounting points for only one USB port, but it outputs up to an amp so it can probably be split between a few devices to run and power.

I'm also contemplating printing a new, smaller case for the Pi and maybe adding a small [OLED display](https://www.adafruit.com/product/3527) to show network connectivity and CPU statuses.
The latter of these two things is pretty low on my list since the Pi's connectivity is relatively stable and, if there are any issues with it, there's not much I can do without either a connection to it or bigger computer to modify the SD card.

## Closing Thoughts

After having written the majority of the post using my Kindleberry Pi Zero W, I think I can say definitively that this is not for everyone.
Knowing an aspiring writer, they desperately want something like this-- a minimalistic, portable writing station with great battery life.
The [Freewrite](https://getfreewrite.com/), while "neat", is so far out of the realm of possibility at its current price of $500 as to not ever be considered an option.
The login process, as seamless as I've gotten it with using SSH keys instead of a password, is still way too many steps for it to be an option.
The connectivity of everything is also not where it'd need to be for me to trust lending this out for anyone to use.
Even showing my coworkers, the latency of the Kindle's eink screen is too slow for them to be terribly interested.
For me, the limitations of a text-only Raspberry Pi-based interface are just too much for regular use.
All the links and images in this post were added on my desktop after having written it just because using a web browser for that is just about mandatory.
The Kindle's wireless connection also is a little spotty, with frequent disconnects and eventual reconnects.

Still though, there's something that I really like about the minimalism and portability, if not the practicality.
This is probably going to be something that I travel with and use but definitely won't be my only computing device.
Depending on how the MPi3 project goes, it may not even be the only Raspberry Pi that I carry with me.

----

## Update

So after I posted [this on Reddit](https://www.reddit.com/r/raspberry_pi/comments/7psulz/how_i_set_up_my_kindleberry_pi_zero_w_portable/), it got picked up by Hack-A-Day!
I actually found out about [their post on it](https://hackaday.com/2018/01/15/this-portable-pi-may-not-be-what-you-expect/) from my Google Now feed that Monday morning, so that was pretty incredible to wake up to.
After Hack-A-Day, [Adafruit](https://blog.adafruit.com/2018/01/19/kindleberry-pi-zero-w-piday-raspberrypi-raspberry_pi/) and a few other blogs also picked it up.

I had someone reach out to me asking about latency and I recorded the below video showing typing some things and running `htop` and `sl`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/e-dsJA_v6cA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

