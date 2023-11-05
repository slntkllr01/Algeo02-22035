function Card(){
    return(
    // <div className=" ">
        <div className="flex flex-nowrap gap-5 max rounded overflow-hidden shadow-lg p-5">
            <div className="flex-none w-1/3">
                    {<div className="bg-gray-200 p-4 mb-4">
                        <div className="font-bold text-xl mb-2">Card 1</div>
                    </div>}
            </div>
        </div>
    );
}
export default Card;