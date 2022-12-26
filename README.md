# Portable Python Projects
> Run on a Raspaberry Pi 

## TwitchTimer

Usage

```
python3 twitchtimer.py -c [twitch channel] -t [duration in minutes]
```
Example
```
python3 twitchtimer.py -c rtainjapan -t 2 #It will open the channel rtainjapan and the code will run for 2 minutes.
```
### Requirements

#### Hardware

* HDTV display, or computer monitor with HDMI input and built-in speakers.

#### Software

* VLC media player (already installed in Raspberry Pi OS Desktop distribution);
* Streamlink.

Note: You can use it on your desktop too.

## Water Leak Notifier

### Requirements

#### Hardware

* [Floor water sensor](https://www.amazon.com/Floor-Water-Sensor-Flood-Detection/dp/B079YB1T8J)

#### Software

* Gmail (or other IMAP-compliant email) account.


Edit water-Leak.py with your email, password and, if you want, edit the body of the email
