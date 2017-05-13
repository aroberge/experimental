#pylint: disable=C0103, W0212
'''
In the following explanation, when we mention "the console" we refer to
a session using the experimental interactive console included in this package.

Possible invocations of this module:

1. python -m experimental: we want to start the console
2. python -m experimental script: we want to run "script" as the main program
                                but do not want to start the console
3. python -i -m experimental script: we want to run "script" as the main program
                                and we do want to start the console after
                                script has ended
4. python -m experimental trans1 trans2 script: we want to run "script" as the
                                main program, after registering the
                                tansformers "trans1" and "trans2";
                                we do not want to start the console
5. python -i -m experimental trans1 trans2 script: same as 4 except that we
                                want to start the console when script ends

Note that a console is started in all cases except 4 above.
'''
import sys

from .core import console, import_hook, transforms
start_console = console.start_console

if "-m" in sys.argv:
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)-1):
            transforms.import_transformer(sys.argv[i])

        main_module = import_hook.import_main(sys.argv[-1])

        if sys.flags.interactive:
            main_dict = {}
            for var in dir(main_module):
                if var in ["__cached__", "__loader__",
                           "__package__", "__spec__"]:
                    continue
                main_dict[var] = getattr(main_module, var)
            start_console(main_dict)
    else:
        start_console()
