describe('Block', () => {
    const timestamp = 'a-date';
    const lastHas = 'foo-hash';
    const hash = 'bar-hash';
    const data = ['blockchain', 'data'];
    const block = new Block({ 
        timestamp: timestamp,
        lastHash: lastHash,
        hash: hash,
        data: data
    });

    it('has a timestamp, lashHash, hash, and data attribute', () => {
        expect(block.timestamp).toEqual(timestamp);
        expect(block.lastHash).toEqual(lastHash);
        expect(block.hash).toEqual(hash);
        expect(block.data).toEqual(data);
    });
});
