=> dockerize this application.


TO DO'S
1. All database functionality code in seperate file     -> done

2. Function to "list last n recordings"                 -> done

3. speech recognition documentation (pause details)     -> done 

4. timeout for listening (using time_stamp)             -> done

5. giving outputs as audio                              -> done

6. calling different func. by speech                    -> done 
    -> send mail                                        -> done
    -> search in database (text)                        -> done
    -> search in database (date)                        -> done

7. adding duration of recording in table with the       -> done
    recordings                   

8. User Interface   
    -> search options                                   -> done
    -> start button                                     -> done
    -> stop button                                      -> buggy (2)
    -> showing database table with:                     -> done
        - duration of the text recording                -> done
        - date and time                                 -> done
        - first five words of recorded text             -> done
        (when clicked on it shows full text)            -> done

9. different timers for listening for command           -> done
    and when rec. has started

10. a log of operations performed                       -> done
    (recording started, timer and all) on ui.           

11. icon on top left                                    -> good to have

12. heading itself as a button for start/stop           -> good to have

13. in the table latest on top                          -> done

14. pagination (10 recordings on one page)              -> done

15. duration fix (bug)                                  -> done

16. date and time readable manner with small icons ()   -> good to have

17. sumeval lib for summarization & sumy lib.           -> done

18. use summarizer on the ui                            -> done
    follow up - save record summary in db.              -> done

19. have a seperate config file for                     -> must have
    all the configurations

20. top 5 keywords on the basis of freq.                -> done
    (should not contain articles and small words)

21. add a punctuator to effeciently summarize text      -> done