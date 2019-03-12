from concurrent import futures

from flags_sequential import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        todo = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            todo.append(future)
            msg = 'Scheduled fpr {}: {}'
            print(msg.format(cc, future))
        results = []
        for future in futures.as_completed(todo):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many)
