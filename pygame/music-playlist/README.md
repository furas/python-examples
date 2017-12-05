I try to use [queue()](http://pygame.org/docs/ref/music.html#pygame.mixer.music.queue) but it doesn't work for me.
Maybe it needs `for event` loop to work but it doesn't work for me too.

In documentation below [queue()](http://pygame.org/docs/ref/music.html#pygame.mixer.music.queue) I found this comment:

>    This method only queues one music file.  
>    If you call it and there already is a queued file, it will be overrided.

so queue is not so usefull.

I use [pygame.mixer.music.set_endevent()](http://pygame.org/docs/ref/music.html#pygame.mixer.music.set_endevent) with `for event` loop to start next track.


