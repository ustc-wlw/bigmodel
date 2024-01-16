from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(len(cc_list), MAX_WORKERS)
    print('workers number is ', workers)
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    print(res)
    return len(list(res))

if __name__=='__main__':
    main(download_many)