#!/usr/bin/python
from subprocess import Popen, PIPE, STDOUT
from proxy_txt_to_dict import proxy_txt_to_dict
from python_multithreading.multithreading import ThreadManager
from check_if_port_is_open import checkIfPortIsOpen

import argparse

def writeGoodProxiesToFile(good_proxies_list, file_name):
    file = open(file_name, 'w')
    for proxy in good_proxies_list:
        file.write(proxy + '\n')
    file.close()


def main(timeout = 1, nThreads = 10):
    proxy_dict_ip_to_port=proxy_txt_to_dict()
    argument_list=list()
    for proxy in proxy_dict_ip_to_port:
        ip=proxy
        port=proxy_dict_ip_to_port[proxy]
        timeout=1
        argument_list.append([ip, port, timeout])

    thread_manager=ThreadManager(argument_list, 10, checkIfPortIsOpen)
    try:
        thread_manager.run()
    finally:
        thread_manager.join()
        results_list=thread_manager.getResults()
        results=list()
        for result in results_list:
            if result is not None:
                results.append(result)
        print("Proxies that were found to work: ", results)
        writeGoodProxiesToFile(results, 'good_proxies.txt')

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timeout', type=int, default=1, help='Timeout in seconds')
    parser.add_argument('-n', '--nThreads', type=int, default=10, help='Number of threads')
    args = parser.parse_args()
    return args
if __name__ == "__main__":
    args = parseArguments()
    main(args.timeout, args.nThreads)
